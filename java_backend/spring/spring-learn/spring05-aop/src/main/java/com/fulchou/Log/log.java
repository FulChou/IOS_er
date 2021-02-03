package com.fulchou.Log;

import org.springframework.aop.MethodBeforeAdvice;

import java.lang.reflect.Method;

public class log implements MethodBeforeAdvice {
    @Override
    public void before(Method method, Object[] objects, Object target) throws Throwable {
        System.out.println("执行了"+target.getClass().getName()+"的"+method.getName()+" 方法");

    }
}
