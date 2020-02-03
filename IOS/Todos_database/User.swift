//
//  User.swift
//  Todos
//
//  Created by 周福 on 2020/2/3.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import Foundation
import RealmSwift

class User: Object {
    @objc dynamic var name = ""
    @objc dynamic var age = 0
}
