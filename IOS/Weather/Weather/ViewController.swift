//
//  ViewController.swift
//  Weather
//
//  Created by 周福 on 2020/1/29.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit
import CoreLocation
import Alamofire
import SwiftyJSON

class ViewController: UIViewController {
    let locationManager = CLLocationManager()
    
    @IBOutlet weak var locationLabel: UILabel!
    
    @IBOutlet weak var imageview: UIImageView!
    @IBOutlet weak var TLabel: UILabel!
    let weather = Weather()
    let appid = "8f35cb963f3d5396adad5398430612b3"
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        locationManager.delegate = self
        // Do any additional setup after loading the view.
    }
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        locationManager.requestWhenInUseAuthorization()//请求授权当前的位置
        locationManager.desiredAccuracy = kCLLocationAccuracyHundredMeters//设置位置精度，精度越大，越耗电，耗资源。
        locationManager.requestLocation()// 获取位置
        
    }
    
    struct WeatherParameters: Encodable {
        let lat: String
        let lon: String
        let appid:String
    }
    
    
    func updateModel(json:JSON){
        let name = json["name"].stringValue//如果为空，取出来是nil
        let t = Int(round(json["main"]["temp"].doubleValue-273.15))
        
        self.weather.temp = Int(t)
        self.weather.location = name
        self.weather.condition = json["weather",0,"id"].intValue
    }
    
    func updateUI(){
        self.locationLabel.text = weather.location
        self.TLabel.text = "\(weather.temp)˚"
        self.imageview.image = UIImage(named: "\(weather.icon)")
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
        if segue.identifier == "searchCity"{
            let vc = segue.destination as! SearchCityViewController
            vc.currentCity = weather.location
            vc.delegate = self
        }
    }
    func searchWeacher(api:String,parameters:[String:String]){
        AF.request(api,
                   method:.get,parameters:parameters,
                   encoder: URLEncodedFormParameterEncoder.default).response{response in
                    switch response.result {
                    case .success(let value):
                        let json = JSON(value)
                        //传数据到模型
                        self.updateModel(json: json)
                        // 改变视图
                        self.updateUI()
                    case .failure(let error):
                        print(error)
                    }
        }
    }


}
extension ViewController:CLLocationManagerDelegate,SearchCityDelegate{
    
    func didSearchCityBtn(cityName: String) {
//        print(cityName)
        //
        let patameters = ["q":"\(cityName)","appid":appid]
        let api = "https://api.openweathermap.org/data/2.5/weather"
        searchWeacher(api: api, parameters: patameters)
        
    }

    
    
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        print(error)
    }
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
            let lat = locations[0].coordinate.latitude
            let lon = locations[0].coordinate.longitude
        
            
    //        print(lat,lon)
            let api = "https://api.openweathermap.org/data/2.5/weather"
            let weatherPatameter = WeatherParameters(lat: "\(lat)", lon:"\(lon)", appid: appid)
        
//        searchWeacher(api: api, parameters: weatherPatameter) 用的是两种不同的访问方法。
            AF.request(api,
                       method: .get,
                       parameters: weatherPatameter,
                       encoder: URLEncodedFormParameterEncoder .default).response { response in
    //            debugPrint(response)
                        switch response.result {
                           case .success(let value):
    //                        传数据到模型
                            let json = JSON(value)
                            self.updateModel(json: json)
                            // 改变视图
                               self.updateUI()
    //                           print(name)
    //                           print(t)
    //                           print("JSON: \(json)")
                           case .failure(let error):
                               print(error)
                           }
           
            }
            
            
        }
    
}

