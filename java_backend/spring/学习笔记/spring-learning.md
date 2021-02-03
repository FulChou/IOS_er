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

- 显式手动写 java

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

**@Repository：** Dao

**@Service：**Service

**@Controller：**Controller

**@Scope("Singleton")**: 单例，原型

## 6.使用javaConfig来实现配置

纯java的配置：

一个专门的类，用来实现配置，对于@bean： class：方法返回类型， id：方法名。

使用AnnotationConfigApplicationContex类来获取配置文件（config.java）



## 7.代理模式

就是 在不改变原代码的情况下 新增功能。

### 7.1介绍

**意图：**为其他对象提供一种代理以控制对这个对象的访问。

**主要解决：**在直接访问对象时带来的问题，比如说：要访问的对象在远程的机器上。在面向对象系统中，有些对象由于某些原因（比如对象创建开销很大，或者某些操作需要安全控制，或者需要进程外的访问），直接访问会给使用者或者系统结构带来很多麻烦，我们可以在访问此对象时加上一个对此对象的访问层。

**何时使用：**想在访问一个类时做一些控制。

**如何解决：**增加中间层。

**关键代码：**实现与被代理类组合。

**应用实例：** 1、Windows 里面的快捷方式。 2、猪八戒去找高翠兰结果是孙悟空变的，可以这样理解：把高翠兰的外貌抽象出来，高翠兰本人和孙悟空都实现了这个接口，猪八戒访问高翠兰的时候看不出来这个是孙悟空，所以说孙悟空是高翠兰代理类。 3、买火车票不一定在火车站买，也可以去代售点。 4、一张支票或银行存单是账户中资金的代理。支票在市场交易中用来代替现金，并提供对签发人账号上资金的控制。 5、spring aop。

**优点：** 1、职责清晰。 2、高扩展性。 3、智能化。

**缺点：** 1、由于在客户端和真实主题之间增加了代理对象，因此有些类型的代理模式可能会造成请求的处理速度变慢。 2、实现代理模式需要额外的工作，有些代理模式的实现非常复杂。



### 7.2 动态代理

链接：https://www.liaoxuefeng.com/wiki/1252599548343744/1264804593397984

我们仍然先定义了接口`Hello`，但是我们并不去编写实现类，而是直接通过JDK提供的一个`Proxy.newProxyInstance()`创建了一个`Hello`接口对象。这种没有实现类但是在运行期动态创建了一个接口对象的方式，我们称为动态代码。JDK提供的动态创建接口对象的方式，就叫动态代理。

```java
public class Main {
    public static void main(String[] args) {
        InvocationHandler handler = new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                System.out.println(method);
                if (method.getName().equals("morning")) {
                    System.out.println("Good morning, " + args[0]);
                }
                return null;
            }
        };
        Hello hello = (Hello) Proxy.newProxyInstance(
            Hello.class.getClassLoader(), // 传入ClassLoader
            new Class[] { Hello.class }, // 传入要实现的接口
            handler); // 传入处理调用方法的InvocationHandler
        hello.morning("Bob");
    }
}

interface Hello {
    void morning(String name);
}
```

## 8.Spring 中的AOP

Spring 容器帮我们去做 动态代理，我们 只需要写好 真实类，代理接口 需要做的事。然后配置好。就可以使用AOP了

![image-20210202153904255](/Users/vincent/Library/Application Support/typora-user-images/image-20210202153904255.png)

- 实现方式一： 实现api接口

写代理需要做的事情类（实现api接口），写接口类。然后使用xml 文件配置

execution 要执行的位置! (*(修饰词) *(返回值) *(类名) *(方法名) *(参数))

- 实现方式二：自定义切面类，然后让切面类里面的方法，通过xml 配置在业务方法的 before，after 等时机执行
  - 缺点是，无法获得接口，函数名信息
- 实现方式三： 注解：
  - 写一个类，记得托管给 spring 容器
  -  @Aspect：注解
  - @Before: 在之前执行（”execution（）“ ）表达式，指定加入注解的类

## 9. 整合mybatis

### mybatis 基本使用步骤：

1. 编写实体类
2. 编写核心配置文件
3. mapper 对应的的接口
4. 编写mapper.xml, 并且注册到核心配置文件里面
5. 测试

整合到 spring 两种方式：

方式一：

每一个mapper 实现类 注册一个bean的时候，使用set方法 注入一个 SqlSessionTemplate 对象

```xml
    <bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
        <constructor-arg index="0" ref="sqlSessionFactory"/>
    </bean>
```



方式二， mapper 实现类 继承SqlSessionDaoSupport ， 直接 getSqlSession 去使用

``` java

        UserMapper mapper = getSqlSession().getMapper(UserMapper.class);
        return mapper.getUsers();
```

## 10 .声明式事务：aop

事务特性：

### ⑴ 原子性（Atomicity）

　　原子性是指事务包含的所有操作要么全部成功，要么全部失败回滚。

### ⑵ 一致性（Consistency）

　　一致性是指事务必须使数据库从一个一致性状态变换到另一个一致性状态，也就是说一个事务执行之前和执行之后都必须处于一致性状态。

　　拿转账来说，假设用户A和用户B两者的钱加起来一共是5000，那么不管A和B之间如何转账，转几次账，事务结束后两个用户的钱相加起来应该还得是5000，这就是事务的一致性。

### ⑶ 隔离性（Isolation）

　　隔离性是当多个用户并发访问数据库时，比如操作同一张表时，数据库为每一个用户开启的事务，不能被其他事务的操作所干扰，多个并发事务之间要相互隔离。

　　即要达到这么一种效果：对于任意两个并发的事务T1和T2，在事务T1看来，T2要么在T1开始之前就已经结束，要么在T1结束之后才开始，这样每个事务都感觉不到有其他事务在并发地执行。

### ⑷ 持久性（Durability）

　　持久性是指一个事务一旦被提交了，那么对数据库中的数据的改变就是永久性的，即便是在数据库系统遇到故障的情况下也不会丢失提交事务的操作

添加事务管理器，然后设置事务切面（给某些方法名，加入事务管理）通过aop 织入，给某一些类加入事务管理功能。

![image-20210203164648334](/Users/vincent/Library/Application Support/typora-user-images/image-20210203164648334.png)

或直接按照官方文档，配置直接 全局事务。

```xml
<tx:jta-transaction-manager />
```





