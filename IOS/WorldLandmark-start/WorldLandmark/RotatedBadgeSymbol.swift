//
//  RotatedBadgeSymbol.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/12.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import SwiftUI

struct RotatedBadgeSymbol: View {
    let angle: Angle
    
    var body: some View {
        BadgeSymbol()
                .padding(-60)
                .rotationEffect(angle, anchor: .bottom)
        }
    
}

struct RotatedBadgeSymbol_Previews: PreviewProvider {
    static var previews: some View {
        RotatedBadgeSymbol(angle: .init(degrees: 3))
    }
}
