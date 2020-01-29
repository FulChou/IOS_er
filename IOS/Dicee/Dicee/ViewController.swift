//
//  ViewController.swift
//  Dicee
//
//  Created by 周福 on 2020/1/7.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet var diceeImageView1: UIImageView!
    
    @IBOutlet var diceeImageView2: UIImageView!
    
    var index1 = 0;
    var index2 = 0;
    let diceArray = ["dice1","dice2","dice3","dice4","dice5","dice6"]
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        updateDiceImage()
        // Do any additional setup after loading the view.
    }

    @IBAction func roll(_ sender: Any) {
        updateDiceImage()
         
        
    }
    func updateDiceImage(){
        index1 = Int.random(in: 0...5)
        index2 = Int.random(in: 0...5)
        diceeImageView1.image = UIImage(named: diceArray[index1])
         diceeImageView2.image = UIImage(named: diceArray[index2])
    }
    override func motionBegan(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        updateDiceImage()
    }
    
}

