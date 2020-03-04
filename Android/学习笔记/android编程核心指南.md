# android编程指南入门学习：

## 第一章：

- 新建android项目，修改xml文件-修改项目的控件
- layout中的xml引用values文件夹中的strings.xml，通过"@string/false_button"
- android studio Session 'app': Error Installing APK解决方法
  - 尝试Build -> Clean Project再编译。
- 在activity中引用已经xml生成的组件：public View findViewById(int id)
- android 应用属于典型的事件驱动类型：
  - 使用匿名内部类来实例化监听器，监听器是首先特定监听器接口的对象
- Android的toast
是用来通知用户的简短弹出消息，用户无需输入或进行任何操作。

Gradle编译android项目：
1. 进入项目目录
2. ./gradlew tasks //编译项目
3. ./gradlew installDebug // 安装项目到当前连接的设备上



