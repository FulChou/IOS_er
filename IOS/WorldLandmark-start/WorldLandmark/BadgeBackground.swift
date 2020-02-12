//
//  BadgeBackground.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/12.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

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
