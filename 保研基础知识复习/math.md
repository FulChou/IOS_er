
## [三个中值定理](https://zhuanlan.zhihu.com/p/47436090)

- 罗尔中值定理：


设函数满足以下三个条件：
1. $f(x)$ 在闭区间[a,b] 上连续
2. $f(x)$ 在开区间(a,b) 上可导
3. $f(a)=f(b)$
则存在$\epsilon \in$(a,b)，使得$f(\epsilon)'=0$
![](img/math/math-2020-07-11-10-57-14.png)

- 拉格朗日中值定理:

设函数满足以下三个条件：
1. $f(x)$ 在闭区间$[a,b]$ 上连续
2. $f(x)$ 在开区间$(a,b)$ 上可导
<!-- 3. $f(a)=f(b)$ -->
则存在$\epsilon \in$(a,b)，使得$f(\epsilon)'= \frac{f(b)-f(a)}{b-a}$

罗尔中值定理 是 拉格朗日的特例。

- 柯西中值定理:

设函数$f(x),g(x)$满足以下条件：
1. $f(x),g(x)$ 在闭区间$[a,b]$ 上连续
2. $f(x),g(x)$ 在开区间$(a,b)$ 上可导
3. $\forall x \in (a,b)$ 有：$g(x)'\not ={0}$

则存在$\epsilon \in(a,b)$ ，使等式$\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f(\epsilon)'}{g(\epsilon)'}$
成立。

如果：
$$
f(x)=f(x) \\
g(x)=x
$$

那么柯西中值定理就变为了拉格朗日中值定理，所以拉格朗日又是柯西的特例。

## [中心极限定理含义？数据如何处理?](https://zhuanlan.zhihu.com/p/25241653)

**什么是中心极限定理（Central Limit Theorem）**

中心极限定理指的是给定一个任意分布的总体。我每次从这些总体中随机抽取 n 个抽样，一共抽 m 次。 然后把这 m 组抽样分别求出平均值。 这些平均值的分布接近正态分布。

why? [证明](https://zhuanlan.zhihu.com/p/93738110)