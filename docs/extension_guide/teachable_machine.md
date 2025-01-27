# Tutorial

## 介绍

[CodeLab Adapter 接入 Teachable Machine](https://www-old.codelab.club/blog/adapter-teachable-machine/)

{!utils/dependence.md!}


## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2：打开 Teachable Machine

Longan团队已经将Teachable Machine部署到国内: [Longan Teachable Machine](https://train.longan.link/), 并且内置支持CodeLab Adapter， 开箱可用！

!!! 提醒
    海外用户参考文末操作

![](/img/16b68d4ed7a09777342a827d26282050.png)

表示已经将  Teachable Machine 接入 CodeLab Adapter 了。

接下来，可以开始你的 Teachable Machine 之旅途。 我们来展示一个例子。

![](/img/tm_demo.png)

## 步骤 3：打开 [Codelab Scratch3](https://scratch-beta.codelab.club/)

{!utils/open_scratch.md!}

接着在 Scratch 中拿到 Teachable Machine 的训练结果，构建一个简单应用。

![](/img/WechatIMG569.png)

在线打开它 [tm_scratch_demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-tm-new.sb3)

!!! tips
    来自Teachable Machine的消息，源源不断流过来，有时候你并不希望重复触发同一件事。可以参考以下例子 [Scratch-tm-latest-class](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-tm-latest-class.sb3) 。

!!! 提醒
    Teachable Machine 的网页不能在后台运行，需要和 Scratch 一起并列在桌面上，否则程序不会运行。


# 海外用户

如果你是海外用户，建议使用 [Google 官方的 teachablemachine](https://teachablemachine.withgoogle.com/)， 你需要搭配以下插件。  

安装 Chrome 浏览器插件：[Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)。    

点击安装 Tampermonkey 脚本 [Teachablemachine_Result.user.js](https://gist.githubusercontent.com/wwj718/78402d0de9efb8d33742c8770056489c/raw/2b99784ff8cf0d344e86e8c2b781b0babfc84c33/Teachablemachine_Result_fixed.user.js)。

运行Adapter之后如何页面弹出，已连接Adapter，则说明一切正常