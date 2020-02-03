//
//  TodosCell.swift
//  Todos
//
//  Created by 周福 on 2020/2/1.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit

class TodosCell: UITableViewCell {

    @IBOutlet weak var checkMark: UILabel!
    @IBOutlet weak var todoLabel: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
