//
//  ViewController.swift
//  WebView
//
//  Created by 周福 on 2020/2/28.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit
import WebKit
import LeanCloud

class ViewController: UIViewController {

    @IBOutlet weak var webView: WKWebView!
    var url = "https://www.qq.com"
    var  string : LCString!
    override func viewDidLoad() {
        super.viewDidLoad()
//        webView = WKWebView(frame: self.view.frame)
        webView.navigationDelegate = self
        
        let query = LCQuery(className: "Todos")
        let _ = query.get("5e562717844bb4008e8cb91f") { (result) in
            switch result {
            case .success(object: let todos):
                // todo 就是 objectId 为 582570f38ac247004f39c24b 的 Todo 实例
                
                let string = todos.get("URL") as! LCString
                self.url = string.value
                self.loadURL(urlString: self.url)
                // 获取内置属性
//                let objectId  = todo.objectId
//                let updatedAt = todo.updatedAt
//                let createdAt = todo.createdAt
            case .failure(error: let error):
                print(error)
            }
        }

//        print(url)
//        loadURL(urlString: url)
        // Do any additional setup after loading the view.
    }
    
    private func loadURL(urlString: String) {
        let url = URL(string: urlString)
        if let url = url {
            let request = URLRequest(url: url)
            // init and load request in webview.
            webView.load(request)
                self.view.addSubview(webView)
                self.view.sendSubviewToBack(webView)
            
        }
    }


}

extension ViewController : WKNavigationDelegate{
    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
          print(error.localizedDescription)
      }
      func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
          print("Strat to load")
      }
      func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
          print("finish to load")
      }
}

