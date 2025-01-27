# overdrive
import asyncio
import json
import time
# from bleak import BleakScanner, BleakClient, BleakError
try:
    from bleak import BleakScanner, BleakClient, BleakError  # 有些windows无法使用
except Exception:
    pass
from codelab_adapter_client import AdapterNodeAio
from codelab_adapter_client.thing import AdapterThing
from codelab_adapter_client.utils import is_win
from codelab_adapter_client.config import settings
from codelab_adapter.ble_overdrive import CarProxy

from loguru import logger
debug_log = str(settings.NODE_LOG_PATH / "overdrive.log")
logger.add(debug_log, rotation="1 MB", level="DEBUG")

# todo 尚未支持Linux， ExtensionAio

# Class for the controller
class Drive(AdapterThing):
    def __init__(self, node_instance):
        super().__init__(thing_name="overdrive", node_instance=node_instance)
        self.is_connected = False
        self.task = None

    async def list(self, timeout=5) -> list:
        logger.debug("list devices...")
        try:
            devices = await BleakScanner.discover()  # todo except
        except BleakError as e:
            # 提醒开启蓝牙
            await self.node_instance.pub_notification(str(e), type="ERROR")
            return []
        logger.debug(f'devices: {devices}')
        # 单独处理windows，bleak系统兼容不好
        if is_win():
            device_flag = "link manager protocol"  # lmp
        else:
            device_flag = "drive"
            
        return [str(d.address) for d in devices if device_flag in str(d).lower()]
        
    async def _send_connect_reply(self):
        #  from RVR
        payload = self.node_instance.connect_payload
        payload["content"] = "ok"
        message = {"payload": payload}
        self.node_instance.logger.debug("send connect reply")
        await self.node_instance.publish(message)

    async def _send_disconnect_message(self):
        await self.node_instance.pub_notification(
            f'{self.node_instance.NODE_ID} 已断开', type="WARNING")

    async def _connect(self, address):
        async with BleakClient(address) as client:
            await client.is_connected()
            # 连接成功反馈
            await self._send_connect_reply()
            self.is_connected = True
            self.thing = CarProxy(client, self.node_instance)  # instance, await
            await self.thing.turnOnSdkMode()
            await client.start_notify(self.thing.Anki_Drive_Vehicle_Service_READ, self.thing.notification_handler)
            await asyncio.sleep(0.1)
            while await client.is_connected() and self.is_connected:
                await asyncio.sleep(0.1)
            await self._send_disconnect_message()

    async def connect(self, address, timeout=5):
            # todo 超过5秒没有连上，前端会认为连上？
            # self.thing = BleakClient(address)
            # as task
            # 等待future， 外部停掉
            self.task = asyncio.create_task(
                self._connect(address))  # todo 真正连上后发出
            # await asyncio.sleep(3)
            await asyncio.sleep(timeout)  # 不要答复
            # return True

    async def status(self):
        pass

    async def disconnect(self):
        if self.task:
            self.task.cancel()  # 让用户知道错误信息
        self.is_connected = False
        self.thing = None
        return True

    ### 以下是具体设备驱动


class MyNode(AdapterNodeAio):
    NODE_ID = "eim/node_overdrive"
    HELP_URL = "https://adapter.codelab.club/extension_guide/overdrive/"
    DESCRIPTION = "overdrive"
    VERSION = "0.1.0"  # 设备掉线通知

    def __init__(self):
        super().__init__(logger=logger, bucket_token=300, bucket_fill_rate=300)
        self.thing = Drive(self)
        self.connect_payload = None

    async def run_python_code(self, code):
        try:
            output = await eval(
                code,
                {"__builtins__": None},
                {
                    "car": self.thing.thing,  # 推送风格
                    "connect": self.thing.connect,
                    "disconnect": self.thing.disconnect,
                    "list": self.thing.list,
                })
        except Exception as e:
            output = e
        return output

    async def extension_message_handle(self, topic, payload):
        self.logger.info(f'code: {payload["content"]}')
        python_code = payload["content"]
        if python_code.startswith('connect('):
            # connect
            self.connect_payload = payload
        output = await self.run_python_code(python_code)
        try:
            output = json.dumps(output)
        except Exception:
            output = str(output)
        if not python_code.startswith('connect('):
            # connect 连上之后（异步）发送
            payload["content"] = output
            message = {"payload": payload}
            await self.publish(message)

    def run(self):
        while self._running:
            time.sleep(0.5)

    async def terminate(self, **kwargs):
        try:
            await self.thing.disconnect()
        except Exception:
            pass
        await super().terminate(**kwargs)


if __name__ == "__main__":
    try:
        node = MyNode()
        asyncio.run(node.receive_loop())  # CPU?
    except Exception:
        if node._running:
            asyncio.run(node.terminate())

# export = ArduinoGateway