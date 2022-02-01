#### WeChat-AutoSendBless
- 主要为了过年时，根据微信好友性别或者其他信息，分别自动化送上个性祝福

### 实现工具

#### PC端
- 采用RapidOCR定位元素+pyautogui自动发送
- 安装步骤
  1. 安装所需库
   ```bash
   pip install rapidocr-1.0.0-py3-none-any.whl
   ```
  2. 运行
    ```bash
    python WeChat_PC.py
    ```


#### 安卓手机
##### 方案一：Auto.js(仅限安卓)
- [hyb1996/Auto.js](https://github.com/hyb1996/Auto.js)
- [Auto.js文档](https://hyb1996.github.io/AutoJs-Docs/)
- [Auto.js 4.1.1 Alpha2 APK](https://pan.baidu.com/s/167Vq-2754NIo054PPOdtWg) 提取码：z4bh

##### 方案二：uiautomator2(仅限安卓) 目前采用的✧✧✧

- [openatx/uiautomator2](https://github.com/openatx/uiautomator2)

##### 方案三：Appium(跨平台)

- [Appium官方介绍](http://appium.io/docs/cn/about-appium/intro/)

#### 欢迎大家PR

#### 灵感来源
- [30行代码实现蚂蚁森林自动”偷“能量](https://mp.weixin.qq.com/s/z4rF7XkgQyIh96Ep6XbpIg)

