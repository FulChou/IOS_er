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
// 求next 数组：
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
	int i = 0; 
	int j = 0;

	while (i < strlen(t) && j < strlen(p)) // i是否匹配超过字符串长度，是否匹配到目前的pattern
	{
		if (j == -1 || t[i] == p[j]) 
		{
			i++;
         j++;  // 匹配到了一个字符
		}
	 	else // 没有匹配到，所以转到下一个位置
           		j = next[j];
    	}

    if (j == strlen(p))
       return i - j;
    else 
       return -1;
}
```
12. 一个数的因子：就是从i到这个数（不包括本身）能够整除到数。 比如6 的因子是： 1 2 3

