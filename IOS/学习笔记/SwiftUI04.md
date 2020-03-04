# 苹果官方网站SwiftUI教程04：

[课程地址](https://developer.apple.com/tutorials/swiftui/drawing-paths-and-shapes)

## Drawing Paths and Shapes

- 新建Create a Badge View
- 画徽章的背景图（使用官网的附件代码）
- 在Badge.swfit文件中显示路径，并且填充黑色
- 将六边形点参数位置描绘出来
- 使用addQuadCurve(to:control:)方法为徽章的角绘制Bezier曲线。
- 将徽章路径包装在GeometryReader中，以便徽章可以使用其包含视图的大小，该视图定义大小而不是硬编码值（100）
- 将aspectRatio(_:contentMode:)修改器应用到渐变填充。
- 画徽章的符号，将之前的代码移到BadgeBackground.swfit文件中去
- Create a new custom view called BadgeSymbol for the mountain shape that’s
- 画山峰和上。
- 给符号上颜色，
- Combine the Badge Foreground and Background
- 将图像重复旋转的放在背景上就制作好了
- zstack：

![](img/SwiftUI04/SwiftUI04-2020-02-12-22-01-09.png)

代码片段：

```swift
import SwiftUI

struct BadgeBackground: View {
    // 徽章的背景颜色：
    static let gradientStart = Color(red: 239.0 / 255, green: 120.0 / 255, blue: 221.0 / 255)
    static let gradientEnd = Color(red: 239.0 / 255, green: 172.0 / 255, blue: 120.0 / 255)
    
    var body: some View {
        // 通过几何阅读器来改变图像大小：
        GeometryReader { geometry in
            Path { path in
                // 定义画笔的起点：
                var width: CGFloat = min(geometry.size.width, geometry.size.height) // 定义几何体最小边为宽和长
                let height = width
                let xScale: CGFloat = 0.832
                let xOffset = (width * (1.0 - xScale)) / 2.0
                width *= xScale
                
                path.move(
                    to: CGPoint(
                        x: xOffset + width * 0.95,
                        y: height * (0.20 + HexagonParameters.adjustment)
                    )
                )
                // 画出基本的六边形参数中的点：
                HexagonParameters.points.forEach {
                    path.addLine(
                        to: .init(
                            x: xOffset + width * $0.useWidth.0 * $0.xFactors.0,
                            y: height * $0.useHeight.0 * $0.yFactors.0
                        )
                    )
                    // 给徽章的角绘制Bezier曲线。通过addQuadCurve方法。
                    path.addQuadCurve(
                        to: .init(
                            x: xOffset + width * $0.useWidth.1 * $0.xFactors.1,
                            y: height * $0.useHeight.1 * $0.yFactors.1
                        ),
                        control: .init(
                            x: xOffset + width * $0.useWidth.2 * $0.xFactors.2,
                            y: height * $0.useHeight.2 * $0.yFactors.2
                        )
                    )
                    
                }
                
            }
                //            .fill(Color.black)
                // 渐变的颜色填充
                .fill(LinearGradient(
                    gradient: .init(colors: [Self.gradientStart, Self.gradientEnd]),
                    startPoint: .init(x: 0.5, y: 0),
                    endPoint: .init(x: 0.5, y: 0.6)
                ))
                .aspectRatio(1, contentMode: .fit)
        }
        
    }
}

struct BadgeBackground_Previews: PreviewProvider {
    static var previews: some View {
        BadgeBackground()
    }
}

import SwiftUI

struct BadgeSymbol: View {
    static let symbolColor = Color(red: 79.0 / 255, green: 79.0 / 255, blue: 191.0 / 255)
    
    var body: some View {
        
        
        
        GeometryReader { geometry in
            // 画出山峰：
            Path { path in
                let width = min(geometry.size.width, geometry.size.height)
                let height = width * 0.75
                let spacing = width * 0.030
                let middle = width / 2
                let topWidth = 0.226 * width
                let topHeight = 0.488 * height
                // 绘制山顶：
                path.addLines([
                    CGPoint(x: middle, y: spacing),
                    CGPoint(x: middle - topWidth, y: topHeight - spacing),
                    CGPoint(x: middle, y: topHeight / 2 + spacing),
                    CGPoint(x: middle + topWidth, y: topHeight - spacing),
                    CGPoint(x: middle, y: spacing)
                ])
                // 添加山低下的细节，
                path.move(to: CGPoint(x: middle, y: topHeight / 2 + spacing * 3))
                path.addLines([
                    CGPoint(x: middle - topWidth, y: topHeight + spacing),
                    CGPoint(x: spacing, y: height - spacing),
                    CGPoint(x: width - spacing, y: height - spacing),
                    CGPoint(x: middle + topWidth, y: topHeight + spacing),
                    CGPoint(x: middle, y: topHeight / 2 + spacing * 3)
                ])
            }
            .fill(Self.symbolColor)
        }
    }
}

struct BadgeSymbol_Previews: PreviewProvider {
    static var previews: some View {
        BadgeSymbol()
    }
}

import SwiftUI

struct Badge: View {
     static let rotationCount = 8
    
    var badgeSymbols: some View {
//        RotatedBadgeSymbol(angle: .init(degrees: 0))
//            .opacity(0.5)
        // 旋转添加到所有图像
        ForEach(0..<Badge.rotationCount) { i in
                   RotatedBadgeSymbol(
                       angle: .degrees(Double(i) / Double(Badge.rotationCount)) * 360.0
                   )
               }
               .opacity(0.5)
    }
    
    var body: some View {
        ZStack{
            BadgeBackground()
            // badge too large for the backgroud
            GeometryReader { geometry in
                self.badgeSymbols
                    .scaleEffect(1.0 / 4.0, anchor: .top)//??
                    .position(x: geometry.size.width / 2.0, y: (3.0 / 4.0) * geometry.size.height)
            }
        }.scaledToFit()
        
    }
}

struct Badge_Previews: PreviewProvider {
    static var previews: some View {
        Badge()
    }
}

//填充颜色代码理解：
// 渐变的颜色填充
                .fill(LinearGradient(
                    gradient: .init(colors: [Self.gradientStart, Self.gradientEnd]), //指定开始和结束的颜色
                    startPoint: .init(x: 0.5, y: 0), // 指定开始渐变的起点，小数值的在左边上边
                    endPoint: .init(x: 0.5, y: 0.6)  // 指定结束渐变的起点，小数值的在左边上边
                ))

```