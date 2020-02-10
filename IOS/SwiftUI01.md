
# 苹果官方网站SwiftUI教程：

https://developer.apple.com/tutorials/swiftui/creating-and-combining-views

## Creating and Combining Views

- 创建并且组合视图：
- 下载官网素材：[地址](https://docs-assets.developer.apple.com/published/0901712034/CreatingAndCombiningViews.zip)
- 创建一个新的工程，使用swiftUI，并且使用 canvas
- 刷新canvas 快捷键：command-option-p
- 通过代码，canvas使用command-click or 在右边属性进行修改，或者拖入控件modifier来装饰or修饰我们的控件（Text，Image）
- 使用 Vstack Hstack Zstack 从垂直，水平，前后来进行组合控件，因为一个body只能返回一个view
- Spacer（）：是一个可以无限延伸的占位符控件
- .padding()：修饰器，对用一个stack中的组建加点间隔
- 控件可以一直使用多个装饰器（一直点下去）
- .stroke(Color.gray, lineWidth: 4)) 加边框
- .shadow(radius: 10) 加阴影
- 同时使用uikie和SwiftUI
- 视图需要遵循UIViewRepresentable协议
- 并且实现两个函数：```makeUIView(context:),updateUIView(_:context:)```
- 组合视图：
- 在contentview中添加：MapView（）.frame(width:height:)//只需要
- 组合MapView，CircleImage，Text

```swift
//contentView.swift
 var body: some View {
        VStack {
            MapView(coordinate: landmark.locationCoordinate)
                .frame(height: 300)
                .edgesIgnoringSafeArea(.top)//忽略安全区域
            
            CircleImage(image: landmark.image)                
            .offset(y: -130)
                .padding(.bottom, -130)
            
            VStack(alignment: .leading) {
                Text(landmark.name)
                    .font(.title)
                
                HStack(alignment:.top) {
                    
                    Text(landmark.park)                        
                    .font(.subheadline)
                    Spacer()
                    Text(landmark.state)                        
                    .font(.subheadline)
                    
                }
            }
            .padding()
            
            Spacer() //将视图推到top of the screen
        }
        .navigationBarTitle(Text(landmark.name), displayMode: .inline)
    }
```

具体可以结合项目 地址：[WorldLandMark](https://github.com/CSUpengyuyan/IOS_er/tree/master/IOS/WorldLandmark)

