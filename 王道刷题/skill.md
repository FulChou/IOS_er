# 技巧

1. 年月日问题，预处理日期数组；
   1. int datas[2][12]={{31,28,31,30,31,30,31,31,30,31,30,31},
                  {31,29,31,30,31,30,31,31,30,31,30,31}};
2. 闰年的条件： （year%4==0&&year%100!=0)||year%400==0;
3. 处理日期程序要注意，虽然叫2月但是只过了1月的整月，虽然只过了11个整月要叫12月；
4. 转译符号是左上到右下。 '\n'
5. 小技巧：
```c++
// #define leap(x) (x%400==0||(x%4==0&&x%100!=0)?1:0)
// #define Abs(x) ((x)>0?(x):-(x))
// typedef struct date
// {
//     int y, m, d;
// }Date;
// Date x ;
```

6. scanf 别忘了 `scanf("%d",&n)`中的&；
7. printf("%04d-%02d-%02d\n",year,month,day)
8. 判断一个数字的奇偶：
   1. (i&1) 是按位 与 运算,相当于 取出 i 的2 进制数值的个位数。 如果 i 是 十进制 奇数，i&1 得 1； 如果 i 是 十进制 偶数，i&1 得 0

9. sort 自定义cmp函数法则：

当比较函数返回true时，表示的是比较函数的第一个参数将会排在第二个参数前面。

10. sort(a,a+n,greater<int>())// 从大到小排序。
11. KMP字符串匹配算法：
```c++
// 求next 数组：，扫描一遍patter来求next数组；
void getNext(char * p, int * next)
{
	next[0] = -1;
	int i = 0, j = -1; // i is index , j is value;

	while (i < strlen(p))
	{
		if (j == -1 || p[i] == p[j])
		{
			++i;
			++j;
			next[i] = j; // 如果当前的字符一致
		}	
		else
			j = next[j]; 
	}
}
// 进行kmp算法：
int KMP(char * t, char * p) 
{
	int i = 0;  // index of t
	int j = 0;  // index of pattern

	while (i < strlen(t) && j < strlen(p)) // i是否匹配超过字符串长度，是否匹配到目前的pattern
	{
		if (j == -1 || t[i] == p[j])   // 已经匹配的长度
		{
			i++;
         	j++;  // 匹配到了一个字符
		}
	 	else // 没有匹配到，所以转到下一个位置
           		j = next[j];
    }

    if (j == strlen(p))
       return i - j; // 找到了第一个的位置
    else 
       return -1；
}
```
12. 一个数的因子：就是从i到这个数（不包括本身）能够整除到数。 比如6 的因子是： 1 2 3
13. 最大公约数：最小公倍数（两数的乘积 / 两数的最小公倍数）

```c++
//greatest common Divisor
int GCD(int a,int b){//辗转相除法
    if(b==0){
        return a;
    }else return GCD(b, a%b);
}
```
14. 质数：一个数x 从2开始到sqrt（x） 都不能整除 x。那么这个x是质数。
15. 因数： 约数的个数等于所有 质因数指数+1 的乘积。
    1.  由约数个数定理可知378000共有正约数(4+1)×(3+1)×(3+1)×(1+1)=160个。
16. 数据绝对值介于1~10^9 ：int型 ｜｜ 10^9~10^18 ：long long型

17. 现代计算机的计算能力与时间复杂度：

1s能完成的运算次数是10^7~10^8。对于规模n=1000的数据，以及采用O(n^2)的算法，则产生的运算次数为10^6级别，在可承受范围之内。但若改为n=10000的数据，则必须将复杂度降到O(n)或以下，否则程序评测时必定产生超时错误。
空间复杂度
不能开数个10^7以上的数组空间，一般情况下10^6的数组空间就足够用了。对于较大的数组（10^4及以上的数组）都要放到全局空间中开辟，不能放到主函数或其他函数中开辟，否则将发生爆栈错误。

18. 计算代码运行时间：
```c++
    clock_t start, end;
    start = clock();
    test(10);// 运行代码
    end = clock();
    cout<<"Run time: "<<(double)(end - start) / CLOCKS_PER_SEC<<"S"<<endl; // 头文件ctime
```
