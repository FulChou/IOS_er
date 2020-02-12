//
//  UserData.swift
//  WorldLandmark
//
//  Created by 周福 on 2020/2/10.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import SwiftUI
import Combine

final class UserData: ObservableObject  {
    @Published var showFavoritesOnly = false
    @Published var landmarks = landmarkData
}
//SwiftUI subscribes to your observable object, and updates any views that need refreshing when the data changes.
