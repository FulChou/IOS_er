package com.fulchou.Log;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class AnnotationAop {

    @Before("execution(* com.fulchou.Service.*.*(..))")
    public void atBefore(){
        System.out.println("这个是 注解的 方法执行前：");
    }

}
