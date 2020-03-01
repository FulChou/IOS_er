//
//  AppDelegate.swift
//  WebView
//
//  Created by 周福 on 2020/2/28.
//  Copyright © 2020 zf.org.csu. All rights reserved.
//

import UIKit
import LeanCloud

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {



    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        do {
            try LCApplication.default.set(
                id: "V7WkXMqS8N2JxhgKnUWWuvXX-gzGzoHsz",
                key: "xMs4E8xcP9h0daS2qve7pAp3",
                serverURL: "https://v7wkxmqs.lc-cn-n1-shared.com")
        } catch {
            print(error)
        }
        
        return true
    }

    // MARK: UISceneSession Lifecycle

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }

    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
    }


}

