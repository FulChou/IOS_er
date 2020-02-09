//
//  LandmarkRow.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/10.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import SwiftUI

struct LandmarkRow: View {
    var landmark: Landmark
    
    var body: some View {
        HStack {
            landmark.image
                .resizable()
                .frame(width: 50, height: 50)
            Text(landmark.name)
            Spacer()
            
        }
    }
}

struct LandmarkRow_Previews: PreviewProvider {
    // The code you write in a preview provider only changes what Xcode displays in the canvas.
    static var previews: some View {
        
//   Group {
//            LandmarkRow(landmark: landmarkData[0])
//                .previewLayout(.fixed(width: 300, height: 70))
//            LandmarkRow(landmark: landmarkData[1])
//                .previewLayout(.fixed(width: 300, height: 70))
//        }
        
//        Group {
//            LandmarkRow(landmark: landmarkData[0])
//            LandmarkRow(landmark: landmarkData[1])
//        }
//        .previewLayout(.fixed(width: 300, height: 70))
        LandmarkRow(landmark: landmarkData[0])
        
    }
}
