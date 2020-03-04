# 苹果官方网站SwiftUI教程02：

[课程地址](https://developer.apple.com/tutorials/swiftui/building-lists-and-navigation)

素材地址：[官方地址](https://docs-assets.developer.apple.com/published/b91dccd475/BuildingListsAndNavigation.zip)

## Building Lists and Navigation

- 给app添加list展示View和界面跳转功能
  - 创建模型文件Landmark.swift
  - 导入landmarkData.json文件，另外写好json转换成类的文件：可以参考我项目中DataUtil.swfit文件 地址：[url](https://github.com/CSUpengyuyan/IOS_er/tree/master/IOS/WorldLandmark-star)
  - 上个项目中的contenView改名为LandmarkDetail文件
  - 新建LandmarkRow.swift.来显示单个row
  - 如果定义变量，那么previews中就需要向里面传值
  - 通过.previewLayout(.fix(width:xx,height:xx))修饰previews
  - Group{}可以显示多组row
  - 创建一个Landmark list
  - List{}or list(数据源){} 数据源需要带唯一的参数id-path
  - 如果数据源遵循 Identifiable协议，那么List数据源不需要带id参数,需要有id属性才能遵循此协议
  - Set Up Navigation Between List and Detail
  - NavigationView{} 嵌套 list
  - .navigationBarTitle(Text("Landmarks"))添加修饰器，添加titie
  - 使用NavigationLink来进行界面跳转，navigationLink（跳转的目的地）{//响应点击的控件}
  - 传递数据到子视图：将一些之前hard code 的数据使用变量来代替，通过调用时传入landmark数据，来动态更新。
![](img/SwiftUI02/%20%20-%20.png)
  - 修改模拟器启动的第一个页面：
  - 修改动态的previews，设置多个previews，和previews的机型：


```swift
// 在 previews属性中
    static var previews: some View {
        //        LandmarkList()
        //        .previewDevice(PreviewDevice(rawValue: "iPhone SE"))
        
        ForEach(["iPhone SE", "iPhone XS Max"], id: \.self) { deviceName in
            LandmarkList()
                .previewDevice(PreviewDevice(rawValue: deviceName))
            .previewDisplayName(deviceName)// 添加设备名字
            // You can experiment with different devices to compare the renderings of your views, all from the canvas.
        }
    }
```


