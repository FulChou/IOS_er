//
//  LandmarkList.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/10.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import SwiftUI

struct LandmarkList: View {
   @EnvironmentObject var userData: UserData
    
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
//            List(landmarkData) { landmark in
                // forEach 使用时的list
            List{
                Toggle(isOn: $userData.showFavoritesOnly) {
                                   Text("Favorites only")
                               } // use $ prefix to access a bingding to a state variable, or onr of its properties.
                
                //                NavigationLink(destination: LandmarkDetail(landmark: landmark)){
                //
                //                    LandmarkRow(landmark: landmark)
                //                }
                
                // filter
                
                //        if !self.showFavoritesOnly || landmark.isFavorite {
                //            NavigationLink(destination: LandmarkDetail(landmark: landmark)) {
                //                LandmarkRow(landmark: landmark)
                //            }
                //                }
                
                // forEach
                ForEach(userData.landmarks) { landmark in
                    if !self.userData.showFavoritesOnly || landmark.isFavorite {
                        NavigationLink(destination: LandmarkDetail(landmark: landmark))
                        {
                            LandmarkRow(landmark: landmark)
                        }
                    }
                }
                
                
            }
            .navigationBarTitle(Text("Landmarks"))
            
        }
        
        
    }
}

struct LandmarkList_Previews: PreviewProvider {
    static var previews: some View {
        // 由于数据转换不成功，那么视图渲染也会有问题
        
                LandmarkList()
                .previewDevice(PreviewDevice(rawValue: "iPhone 8"))
         .environmentObject(UserData())
        
        //多个设备预览比较
        
//        ForEach(["iPhone SE", "iPhone XS Max"], id: \.self) { deviceName in
//            LandmarkList()
//                .previewDevice(PreviewDevice(rawValue: deviceName))
//                .previewDisplayName(deviceName)// 添加设备名字
            
            //         You can experiment with different devices to compare the renderings of your views, all from the anvas.
        //}
    }
}
