//
//  Badge.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/12.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

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
