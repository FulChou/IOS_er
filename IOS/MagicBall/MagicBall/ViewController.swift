//
//  ViewController.swift
//  MagicBall
//
//  Created by 周福 on 2020/1/8.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var ballImageView: UIImageView!
    var imagesArray:[String] = ["ball1","ball2","ball3","ball4","ball5"]
    var index = 0;
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    

    @IBAction func askBtn(_ sender: Any) {
        index = Int.random(in: 0...4)
        ballImageView.image = UIImage(named: imagesArray[index])
        print(index)
    }
    

}

