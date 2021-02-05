package com.fulchou.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class HelloController {
    @RequestMapping(value = "/hello", method = {RequestMethod.GET,RequestMethod.DELETE}) // 配置多种请求方法访问：
    public String hello(@RequestParam("username") String name ,Model model){
        model.addAttribute("msg","zhoufu love lk "+ name);
        return "hello";
    }
    @PostMapping("/hello")
    public String test2(Model model){
        model.addAttribute("msg","zhoufu love lk forever");
        return  "hello";
    }

    @PostMapping("/commit/{a}/{b}")
    public String test3(@PathVariable int a, @PathVariable int b, Model model){
        int res = a + b;
        model.addAttribute("msg","zhoufu love lk forever "+ res);
        return  "hello";
    }
    @PostMapping("/encode")
    public String test4(String name,Model model){

        model.addAttribute("msg","test chinese coding"+ name);

        return "hello";
    }
}
