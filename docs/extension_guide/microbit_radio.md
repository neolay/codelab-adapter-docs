# Tutorial

<!--
!!! 提醒
    使用micro:bit v2的话，需要手动在 makecode 里刷入[固件](/hex/makecode_radio_adapter.hex), Adapter的下个版本(4.2.1)我们将提供更好的支持。
    micro:bit v1 和 micro:bit v2 的radio可以通信。   
    只能用于 makecode radio， makecode radio 与 micropython radio不兼容。   
    Adapter `3.7.4` 支持切换 radio channel。 
-->

## 介绍

我们在 [CodeLab Adapter 深度连接 micro:bit （makecode）生态](https://www-old.codelab.club/blog/codelab-adapter-microbit-deep-connect/)中提到

> 我们将一块 micro:bit 接入电脑，用作中转站（类似 usb dongle），用于在 CodeLab Adapter 和任何 micro:bit 套件做中转站。这里的一个背景知识是，任何的 micro:bit 直接可以通过 radio（简易的无线连接）方便地彼此通信。
> 在这个思路中，获得的一个意外收获是：能让任何电脑与 microbit 无线连接！即便没有蓝牙！

ps：在这个教程中，需要准备 2 块 micro:bit。其中一块用作消息中转（暂且称其为`中转站`），另一块用于实现项目功能（暂且称其为`功能板`）。

## 依赖

{!utils/dependence.md!}

## 步骤 1：hello [MakeCode](https://makecode.microbit.org/#editor)

从一个简单的例子开始：[radio_node](https://makecode.microbit.org/_g1UfcDfv8cKp)（`Adapter > 3.4`）

<!--https://makecode.microbit.org/_4EKALy3hCDcq-->

将上述代码 download 到`功能板`(2 块 micro:bit 中的一块)。

上述代码的功能是:

<!--1. 当`功能板`收到来自 CodeLab Scratch 的消息(`c`)时, 显示一颗爱心。（`scratch -> microbit`）
2. 当`功能板`的`A 按钮`被按下时，发送字符`a`, `B 按钮`被按下时，发送字符`b`（`microbit -> scratch`）
-->

1. 当`功能板`收到来自 CodeLab Scratch 的消息时, 将在矩阵屏上显示出消息。
2. 当`功能板`的`A 按钮`被按下时，发送字符`a`, `B 按钮`被按下时，发送字符`b`（`microbit -> scratch`）， 当用力摇晃时，发送字符`shake`

这样便完成了`Scratch--无线microbot`的双向通信:

    *  `scratch -> microbit`
    *  `microbit -> scratch`

!!!注意
    功能板收到的所有消息都是 **字符串**

## 步骤 2：拔下`功能板`，接上`中转站`，加载固件

<!--新版本 0.4 允许设置 channel https://makecode.microbit.org/_P2297z3f0Pkz-->

使用数据线将`中转站` micro:bit 接入电脑，刷入[固件](https://makecode.microbit.org/_P2297z3f0Pkz)。

<!--带版本 https://makecode.microbit.org/_hq7Ciugx396o-->

<!--旧的固件 https://makecode.microbit.org/_EL20Rp98pHAg-->

<!--v0.5 https://makecode.microbit.org/_dHWL0C8dyCJa-->

!!! 提醒
    Windows 7用户注意，无法发现 micro:bit，需要[安装驱动](/img/mbedWinSerial_16466.exe)（和使用 mu-editor 操作相同）  
    linux 用户注意，CodeLab Adapter 使用 usb 串口与 micro:bit 连接，linux 下，使用 usb 串口需要做权限设置：`sudo chmod 666 /dev/ttyACM0`

## 步骤 3：打开 Codelab Adapter

{!utils/open_adapter.md!}

点击加载 [extension_microbit_radio](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_microbit_radio.py) 插件


## 步骤 4：打开 [Codelab Scratch3](https://scratch-beta.codelab.club/)，构建自己的应用

{!utils/open_scratch.md!}

在此展示一个简单例子：使用 A、B 按钮让角色出现和消失。你可以在线打开它 [radio_hello_world_demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/radio_hello_world_demo.sb3)

## 总结
根据以上的模版，加以调整，你可以自行构建自己的应用。


## 完整项目
### fire！
我们使用 micro:bit 来赋予淘宝上的普通魔杖以魔法。一共需要 3 个 micro:bit，一个用作中转站，一个用作可穿戴手表（micro:bit 绑在表带上），一个用作投石器。

<video width=80% src="/video/wand_catapult_demo.mp4" controls="controls"></video>

<video width=80% src="/video//wand_catapult.mp4" controls="controls"></video>

当我们挥动魔杖时，触发投石器开关，fire！

以下是源码

*  micro:bit
    *  [可穿戴设备源码](https://makecode.microbit.org/_aVqEWK9DXbPR)
    *  [投石器源码](https://makecode.microbit.org/_AyU3211xeEYv)
*  Scratch
    *  [wand_catapult](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/wand_catapult.sb3)


我们来关注下以上 2 个 micro:bit 中信息的流向，

可穿戴设备，信息的流向是：`micro:bit -> Scratch`

投石器信息的流向为：`Scratch -> micro:bit`

!!! 提醒
    运行项目时，记得把 CodeLab Adapter 运行起来。

### Scratch 翻页笔
硬件方面，使用了2个microbit:

-   作为翻页笔的手持的microbit: [固件](https://makecode.microbit.org/_bHLV7q2fK3Hc)
-   作为中转站(dongle)的microbit: [固件](https://makecode.microbit.org/_EL20Rp98pHAg)

它们之间基于 radio 通信（[micro:bit radio](/extension_guide/microbit_radio/)）

Scratch 程序参考 [Scratch-翻页笔-demo.sb3](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-翻页笔-demo.sb3){target=\_blank}


# FAQ
## MacOS 10.15 无法使用
MacOS 用户 @patch 提到 MacOS 10.15 以后启用了SIP（System Integrity Protection系统完整性保护），程序对系统目录无法直接访问了。所以flashing new firmware 时报operation not permitted的错误就是这个问题导致的。  
关掉系统的SIP以后再测试，flashing new firmware这一步成功了

## 反复刷入固件
建议拔掉microbit，再重新插入电脑

## 第一次刷入固件
目前有个bug，插拔microbit之后，可能会重新刷入固件。原因似乎是复合的，应该与node和固件（可以使用https://python.microbit.org/v/2加载固件）都有关，这两部目前都是开放的，欢迎大家修复