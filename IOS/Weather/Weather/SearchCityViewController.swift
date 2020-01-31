//
//  SearchCityViewController.swift
//  Weather
//
//  Created by 周福 on 2020/1/31.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit

protocol SearchCityDelegate {
    func didSearchCityBtn(cityName:String)
}


class SearchCityViewController: UIViewController {
    var currentCity = " "
    
    @IBOutlet weak var inputCityTF: UITextField!
    var delegate:SearchCityDelegate?
    
    @IBOutlet weak var currentCityLabel: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        currentCityLabel.text = currentCity
        // Do any additional setup after loading the view.
    }
    
    @IBAction func searchWearher(_ sender: Any) {
        delegate?.didSearchCityBtn(cityName: inputCityTF.text!)
        dismiss(animated: true, completion: nil)
    }
    
    @IBAction func backup(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
