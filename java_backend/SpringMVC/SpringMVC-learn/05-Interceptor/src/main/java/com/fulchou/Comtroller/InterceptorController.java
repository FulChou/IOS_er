package com.fulchou.Comtroller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class InterceptorController {
    @RequestMapping("/interceptor")
    public String test(){
        System.out.println("控制器中的方法执行了");
        return "hello";
    }
}
