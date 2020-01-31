# lebus教程02

### p47 optional变量:

- 可选型：
  - 有值，等于xxx 或者没有值
  - nil，只能给声明为可选类型的变量赋值
  - 强制确定解包 ！
  - 可选绑定：

``` swift
class FastCar:Car{
    var window:Int? // 可选型变量
    override func drive() {
        super.drive()//调用父类的方法。
        print("开快车")
    }
}

let  fastCar = FastCar()
fastCar.window = 1

if xxx != nil{

}//只有在可选值不为空的时候才执行

//or
if let xxx = 可选变量{
    // 可以使用xxx 作为可选型变量的解包值。
    // 也就是赋值 给xxx 可以取一样的名字
}
```

### p48-57 天气app

不用代码画界面：

- 导入app的icon、图标
- 添加控件
- 添加约束
- 编辑另一个页面：
- 编辑基本的控件和约束之后
- 修改加载页面
- 添加页面跳转

- Cocopods：管理引入的包
  - 快速引入
  - 自动升级包 


- 去官网下载客户端，使用app来进行操作（太贴心了，不过以往的经验是网络带不动）- 使用官方的app，非常的无脑简单好使。不担心网络（首次下载app可能很慢）
- pod init// 创建一个新项目，
- 在 Podfile文件里面写要导入的包就行

- p50 天气api and delegate
-  获取用户的当前位置：
   -  import CoreLocation
- plist: property list
  - Privacy - Location When In Use Usage Description //添加value
- 委托 delegate：
  - CLLocationManager()中只有变量没有方法
  - 使用delegate来使用方法
  - protocol// 协议类似 java里面的接口
  - 实现协议中的方法，然后将变量的delegate绑定到自身，利用自己的变量调用自身的方法。

```swift
// 实现协议里面这个方法：
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let lat = locations[0].coordinate.latitude
        let lon = locations[0].coordinate.longitude
        print(lat,lon)
    }
// 页面出现时调用：
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        locationManager.requestWhenInUseAuthorization()//请求授权当前的位置
        locationManager.desiredAccuracy = kCLLocationAccuracyHundredMeters//设置位置精度，精度越大，越耗电，耗资源。
        locationManager.requestLocation()// 获取位置
```

- 在覆盖viewcontroller 的生存周期方法时，要记得super. 去调用原始的方法。
- p51:使用alamofire 完成http请求
- 使用pod 安装Alamofire
- 注册使用 openweather获得appid
- import Alamofire
```swift
        AF.request("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=8f35cb963f3d5396adad5398430612b3").response { response in
            debugPrint(response)
            print(response.data)
        }

```
- 最终打印出别人服务器给的回应。

- http请求方式（method，get，post，delete）
- 字典（一种数据类型，key:value)
  - swift中，如果value有多种值，那么应该指定变量类型：

``` swift
let dict : [String:Any] = xxx

// 请求的参数解析：
// 定义参数的类型
    struct WeatherParameters: Encodable {
        let lat: String
        let lon: String
        let appid:String
    }
// 使用参数encoded
        let weatherPatameter = WeatherParameters(lat: "\(lat)", lon:"\(lon)", appid: appid )

        AF.request("https://api.openweathermap.org/data/2.5/weather",
                   method: .get,
                   parameters: weatherPatameter,
                   encoder: URLEncodedFormParameterEncoder .default).response { response in
            debugPrint(response)
            // 使用SwiftyJSON来转换数据：
                                switch response.result {
                       case .success(let value):
                           let json = JSON(value)
                             let name = json["sdfs"].stringValue//如果为空，取出来是nil，不能print出来？
                             // string得到类型是可选型，但是stringValue出来是一个确定值
                           print(name)
                           print("JSON: \(json)")
                       case .failure(let error):
                           print(error)
                       }
        }//正常获取到了数据。
```

- 使用拓展包：SwiftJSON功能包。
- 使用多看官方文档
- 展示到界面上即可。
- 实际上还是先创建weather模型（采用MVC架构）
- 计算属性（融合了函数和属性两种功能）**它根据别的属性来确实自己是什么**

``` swift
class Weather{
    var temp = 0
    var condition = 0
    var location = " "
    // 计算出行
    var icon :String{
          switch (condition) {
                 
             case 0...300 :
                 return "tstorm1"
                 
             case 301...500 :
                 return "light_rain"
                 
             case 501...600 :
                 return "shower3"
                 
             case 601...700 :
                 return "snow4"
                 
             case 701...771 :
                 return "fog"
                 
             case 772...799 :
                 return "tstorm3"
                 
             case 800 :
                 return "sunny"
                 
             case 801...804 :
                 return "cloudy2"
                 
             default :
                 return "dunno"
        }
    }
}//模型类
//                        传数据到模型
                           self.weather.temp = Int(t)
                           self.weather.location = name
                           self.weather.condition = json["weather",0,"id"].intValue
                           
                           print(t)
                           
                           // 改变视图
                           self.locationLabel.text = name
                           self.TLabel.text = "\(t)˚"
                           self.imageview.image = UIImage(named: "\(self.weather.icon)")
```

- option + k   打出 ˚
- 优化代码，分离出函数和extension
- p56 将自己新建的view 连接到 viewController上面：
- 跳转 prepare for segue，在跳转前做一些准备，可以判断这个跳转是哪一个
- 然后将跳转之后的目的地转（as）为我们目的地controller的类型
- 三种as
  - as as？as！
  - as 向上转型，是安全合法的
  - as？转成可选型 as！转成确定型，没有的话，失败会报错。 向下转型，可能会失败。
- 得到目标 viewControler对象之后，这样也可以进行界面的传值

```swift
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
        if segue.identifier == "searchCity"{
            let vc = segue.destination as! SearchCityViewController
            vc.currentCity = weather.location
        }
    }
```

- p57 自定义protocol和delegate实现导航的反向传值：
- protocol类似接口，只定义方法。
- 使用方法就是在一个类中 定义protocol的变量
- 另一个类实现类这个接口，也就要实现这个类中的方法。
- 调用顺序是先从定义protocol变量的类，然后到实现这个方法的类。实现这个方法的时候，就可以获得从定义protocol变量的类中获取值。
- 其实感觉就是定义了一个接口，接口里面的函数在另外的一个类进行实现。也就是延迟接口的实现。把实现放到了用户去写。（委托模式）
- 进行app的完善工作：


回到上一个界面：dismiss（）
```swift
  @IBAction func searchWearher(_ sender: Any) {
        delegate?.didSearchCityBtn(cityName: inputCityTF.text!)
        dismiss(animated: true, completion: nil)
    }
// 实现接口中的函数：
    func didSearchCityBtn(cityName: String) {
//        print(cityName)
        let patameters = ["q":"\(cityName)","appid":appid]
        let api = "https://api.openweathermap.org/data/2.5/weather"
        searchWeacher(api: api, parameters: patameters)
    }
```