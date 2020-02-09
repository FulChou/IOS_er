//
//  LandmarkList.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/10.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import SwiftUI

struct LandmarkList: View {
    var body: some View {
        // static
        //        List {
        //            LandmarkRow(landmark: landmarkData[0])
        //            LandmarkRow(landmark: landmarkData[1])
        //        }
        
        //         List(landmarkData, id: \.id) { landmark in
        //             LandmarkRow(landmark: landmark)
        //         }
        
        // use collections of Landmark elements directly.
        NavigationView {
            List(landmarkData) { landmark in
                
                NavigationLink(destination: LandmarkDetail(landmark: landmark)){
                    
                    LandmarkRow(landmark: landmark)
                }
                
            }
            .navigationBarTitle(Text("Landmarks"))
            
        }
        
        
    }
}

struct LandmarkList_Previews: PreviewProvider {
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
}
