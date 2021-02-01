# Spring:

## 1. 思想： 依赖反转！

控制反转，依赖注入。 

控制反转，就是让 控制权，跑到最前面去，然后里面配置文件来构造

依赖注入就是控制反转实现的一个方式， 通过setter 方法来输入依赖的类，

最后spring 采用 .xml 的方式来配置bean，这样，对象就不是自己去new 了，就是通过配置文件去反射出对象（ 配置文件反射对象）

依赖：bean对象的创建依赖于容器！ 注入：bean对象中的所有属性，由容器来注入

## 2. 配置文件新建对象，可以通过：

- 默认无参构造方法
- 下标赋值构造方法
- 参数类型构造方法
- 参数名构造方法

配置文件在加载的时候，就会把所有配置bean 都实例化，不管用没用到（可以懒加载），然后实例化一次之后，第二次也会采用同一个（单例模式）



## 3. spring配置文件说明：

1. alias 别名：
2. bean的配置：Bean 下面的name 也是去别名
3. import： 多个配置文件时，使用import 导入其他的 配置.xml 文件，结果：相同的忽略掉，合并成一个配置文件

- 多种类型都能注入，int，String，map，list ，对象。细节看文档呗

拓展方式 （需要导入约束， 在 xml 文件头加入） ：

- p property命名空间注入： 多个属性注入值
- c constructer 命名空间注入：构造器注入值

## 4. bean 作用域：

1. 单例（Singleton默认）： 全局一个对象
2. 原型 （prototype）：每一次需要，new一个对象
3. request  web开发中才能使用
4. session
5. application 

## 5. bean的自动装配：

三种装配bean的方式：

- 显式手动写 xml

- 显式 手动写java

- 隐式 自动装配bean：


  ### 5.1 byName autowired

​    在xml文件中，此类的 id取得和 另一个类的 set方法一致就行

所以说，xml所有的bean， id要唯一

byname的时候，需要保证所有bean的id唯一，并且这个bean需要和自动导入的set方法的值一致

### 5.2 byType autowired

类似前面

### 5.3 注解 Annotation Autowired：

1. 导入约束
2. 配置注解支持

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <context:annotation-config/>
  	<context:component-scan base-package="com.fulchou"/>

</beans>

```

**@Autowired：**

直接在属性上使用即可, 也可以在set 方法上使用，或者不需要set方法了。

默认是 byType，然后byName （名字，属性名要一样） 的方式：如果重复了，可以使用 @Qualifire 来指定 id

**@Resource**

java的 @Resource 也可以实现自动装配 (name={name}) 指定名字

**@Nulllable**: 字段标记注解， 此字段可以为空

**@Compunent:**  相等于将 bean 写到 ApplicationContext.xml 让IOC容器去管理。

类似的在不同的位置(文件夹)使用不用的注解：

**@Repository：**

**@Service：**

**@Controller：**

**@Scope("Singleton")**: 单例，原型