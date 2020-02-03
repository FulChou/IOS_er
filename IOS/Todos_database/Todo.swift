//
//  Todo.swift
//  Todos
//
//  Created by 周福 on 2020/2/1.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import Foundation
import RealmSwift
//struct Todo :Codable{
//    var name = " "
//    var isChecked = false
//}
class Todo: Object {
    @objc dynamic var name = " "
    @objc dynamic var isChecked = false
    @objc dynamic var createDate = Date()
}
