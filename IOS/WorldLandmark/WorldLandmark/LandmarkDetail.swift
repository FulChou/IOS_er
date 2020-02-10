//
//  LandmarkDetail.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/8.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import SwiftUI

struct LandmarkDetail: View {
    
    var landmark: Landmark
    
    var body: some View {
        VStack {
            MapView(coordinate: landmark.locationCoordinate)
                .frame(height: 300)
                .edgesIgnoringSafeArea(.top)//忽略安全区域
            
            CircleImage(image: landmark.image)                .offset(y: -130)
                .padding(.bottom, -130)
            
            VStack(alignment: .leading) {
                Text(landmark.name)
                    .font(.title)
                
                HStack(alignment:.top) {
                    
                    Text(landmark.park)                        .font(.subheadline)
                    Spacer()
                    Text(landmark.state)                        .font(.subheadline)
                    
                }
            }
            .padding()
            
            Spacer()
        }
        .navigationBarTitle(Text(landmark.name), displayMode: .inline)
    }
}

struct LandmarkDetail_Previews: PreviewProvider {
    static var previews: some View {
        LandmarkDetail(landmark: landmarkData[0])
    }
}
