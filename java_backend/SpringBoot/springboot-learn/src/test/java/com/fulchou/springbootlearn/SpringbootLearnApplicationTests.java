package com.fulchou.springbootlearn;

import com.fulchou.springbootlearn.Pojo.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringbootLearnApplicationTests {

    @Test
    void contextLoads() {
    }

    @Autowired
    User user;

    @Test
    void test1(){
        System.out.println(user);
    }

}
