package com.fulchou.Log;

import org.springframework.aop.AfterReturningAdvice;

import java.lang.reflect.Method;

public class AfterLog implements AfterReturningAdvice {
    @Override
    public void afterReturning(Object ReturnValue, Method method, Object[] objects, Object target) throws Throwable {
        System.out.println("执行了"+method.getName()+"返回结果为："+ReturnValue);
    }
}
