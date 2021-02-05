package com.fulchou.Controller;

import com.alibaba.fastjson.JSON;
import com.fulchou.Pojo.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.tags.EditorAwareTag;

import javax.xml.crypto.Data;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@RestController
public class JsonController {
    @GetMapping("json")
    public String helloJson(){
        String res = "";
        List<User> users = new ArrayList<>();
        for(int i=0; i<5 ;i++){
            User user = new User("zhoufu", i, i ^ 2);
            users.add(user);
        }
        String jsonString = JSON.toJSONString(users);
        Object json = JSON.toJSON(users);
        System.out.println(json);
        Date date = new Date();
        return JSON.toJSONString(users);
    }
}
