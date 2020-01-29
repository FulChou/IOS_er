# lebus 第一天笔记

### p36 实现弹出框功能：

- 建议搜索 apple document alert，可以直接查到苹果官方文档。


``` swift
let alert = UIAlertController(title: "My Alert", message: "This is an alert.", preferredStyle: .alert) 
alert.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Default action"), style: .default, handler: { _ in 
NSLog("The \"OK\" alert occured.")
}))
self.present(alert, animated: true, completion: nil)
```

- completion:写的是一个类似于回调函数
- 在回调函数中，调用全局变量，全局方法。要加一个self
- int to CGFloat的方法：
  - CGFloat（int）

### p38 使用第三方库来完成app：

- 实际开发中，不会做。很麻烦，去github上找一找

- 先下载github上面的代码包到本地
- 工程的bundle，.h,.m文件拖到工程中的一个文件夹下面
- 选中coupe items if needed
- 在桥接文件中， #import “ProgressHYD.h"
- 然后使用即可

### p39 自适应 auto resizing
- inspector:
  - 上下左右间隔，以及长和宽。六个可以操作的地方
  - 可以使得离，左边or右边变得不定死，也可以使得背景图填充满

### p40 stackview 布局

- 如果label中的文字被挤出了省略号。快捷键 command + =（size to fit content）
- 文本离label边缘的间隙：右侧尺子，content insets
- 多选多个label， enbed in stackview
- shift 右击，（快速找到控件）
- stack view 中有一些普遍的对齐属性（左，右，居中）
- 然后就可以整个stack view 来进行左边或者下面自适应了
- 实际操作： 在左边居中了，但是右边preview还是不太对。但是run起来是可以的

### p41 嵌套stackview

- 不断的使用垂直，水平 stack view 将控件放到一起
- stackview中，上下可以拖动换位置

### p42 拉伸，压缩优先级+distrubution

- 在stack view中有的属性：
  - content hugging priority 拉伸
  - content Compression Resistance priority 压缩
- 数字越大优先级越大，1--1000
- 压缩优先级越大，就越不被压缩，也就是压缩优先级大，就不压缩
- 拉伸优先级类似，数值越大，越不被拉伸。
- distribution:
  - 布局中间的距离，或者是按照文字比例等等。。。

### p43 约束constraints

- safe area：
- 添加约束
- [-] 相对与margins开始计数，勾选之后，就对相对与安全区域开始计数
- update frames 更新到你之前定好的约束
- 右侧，可以修改约束的具体值
- 等宽约束，等高约束，可以按住command，进行多选
- 等高，和目前的屏幕进行约束，然后再到右侧中的multipller去改成1：n,first:second
- 缩放字体，自动autoshrink，最小缩放到0.5倍。

### p44 小技巧：

- command + d 复制
- option + 拖拽（复制）
- 复制出来的控件同样会复制之前与代码的连接
- 去掉stack view
  - 先将里面的东西拖出来，然后删掉控件
  - 点击下面的unembed(推荐)

### p45 类与对象，枚举

- 枚举 enum xx{ }
xx 是一种自定义的类型

``` swift
enum Type{
    case sports
    case sedan
    case SUV
}

class Car {
    var color = ''
    var seats = 2
    init(name:String,seat:Int){
        self.name = name
        self.seat = seat
    }
    // func name（参数名字：类型）{}
}
```

- 便利构造器：另外一种构造器，在函数里面跳用初始构造器。

在构造的时候使用默认值，不需要传递全部参数，可以需要传递部分参数

``` swift
    convenience init(){
        self.init(name:"玛莎拉蒂",seat: 2)
    }

    convenience init(name:String){
        self.init(name:name,seat: 2)
    }
    // 在便利构造器中调用初始构造器（构造函数）
````

### p46 继承与重写 override

- 构造一个新的类，继承以往有的类（因为有很多相似性，并且从理解上也应该是子类）
- 拥有父类的属性和函数

``` swift
class FastCar:Car{//继承父类
    override func drive() {
        super.drive()//调用父类的方法。
        print("开快车")//追加新的方法。
    }
    // 重写 drive（）方法
```
