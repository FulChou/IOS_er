# c++ 复习知识：

## 输入字符串，字符 [参考链接](https://www.cnblogs.com/flatfoosie/archive/2010/12/22/1914055.html)

1、**cin>>**         

用法1：最基本，也是最常用的用法，输入一个数字：

注意:>> 是会过滤掉不可见字符（如 空格 回车，TAB 等）
cin>>noskipws>>input[j];//不想略过空白字符，那就使用 noskipws 流控制

用法2：接受一个字符串，遇“空格”、“TAB”、“回车”都结束
```c++
#include <iostream>
using namespace std;
main ()
{
char a[20];
cin>>a;
cout<<a<<endl;
}
```
**2、cin.get()**

用法1： cin.get(字符变量名)可以用来接收字符

用法2：cin.get(字符数组名,接收字符数目)用来接收一行字符串,可以接收空格 字符数目应该包括 '\0';

**3、cin.getline()**   // 接受一个字符串，可以接收空格并输出

延伸：
cin.getline()实际上有三个参数，字符数组名，接受字符数目，结束字符。

cin.getline(接受字符串数组,接受个数包括一个‘\0‘,结束字符)

当第三个参数省略时，系统默认为'\0'。如果将例子中cin.getline()改为cin.getline(m,5,'a');当输入jlkjkljkl时输出jklj，输入jkaljkljkl时，输出jk

**4. getline（cin,string）**
`<string>` 中：getline：需要include string头文件

用法：不会忽略space、tab，遇到Enter就结束
```c++
string line;
getline(cin,line)
```

5.  scanf(): `EOF = -1`
```c++
int a, b;
while (scanf("%d %d", &a, &b) != EOF){
    ...
}

scanf("%4d%2d%2d", &a.y, &a.m, &a.d)!=EOF //读取固定的格式数据：

``` 

6. getchar(); // take the '\n' 
7. 获取一个字符

### c++ 算数计算：

```c++
#include <math.h>
//平方 pow()
int a = pow(4,2);// 4的平方=16
//开方
int b = pow(4,0.5);// 4的平方根=2
int c = sqrt(4);// 4的平方根=2
//整数绝对值
int c = abs(b-c);
//浮点数绝对值
double d = fabs(b-c);
```

## 输出字符的处理知识：

1. cout<<
2. printf()
``` bash
%a  浮点数、十六进制数字和p-记数法（c99
%A  浮点数、十六进制数字和p-记法（c99）
%c  一个字符(char)
%C  一个ISO宽字符
%d  有符号十进制整数(int)（%ld、%Ld：长整型数据(long),%hd：输出短整形。）　
%e  浮点数、e-记数法
%E  浮点数、E-记数法
%f  单精度浮点数(默认float)、十进制记数法（%.nf  这里n表示精确到小数位后n位.十进制计数）
%g  根据数值不同自动选择%f或%e．
%G  根据数值不同自动选择%f或%e.
%i  有符号十进制数（与%d相同）
%o  无符号八进制整数
%p  指针
%s  对应字符串char*（%s = %hs = %hS 输出 窄字符）
%S  对应宽字符串WCAHR*（%ws = %S 输出宽字符串）
%u  无符号十进制整数(unsigned int)
%x  使用十六进制数字0xf的无符号十六进制整数　
%X  使用十六进制数字0xf的无符号十六进制整数
%%  打印一个百分号
```
**说明：** 

%2d：表示输出场宽为2的整数，超过2位按照实际数据输出，不够2位右对齐输出。

%02d:表示输出场宽为2的整数，超过2位按照实际数据输出，不够2为前置补0

%5.2f： 表示输出场宽度为5的浮点数，其中小数点后有两位，不够五位右对齐输出


## c++ String 的用法：[参考链接](https://blog.csdn.net/tengfei461807914/article/details/52203202)

1. 声明：

string s;//声明一个string 对象

string ss[10];//声明一个string对象的数组

2. 初始化：

```c++
    string s;//默认初始化，一个空字符串
    string s1("ssss");//s1是字面值“ssss”的副本
    string s2(s1);//s2是s1的副本
    string s3=s2;//s3是s2的副本
    string s4(10,'c');//把s4初始化
    string s5="hiya";//拷贝初始化
    string s6=string(10,'c');//拷贝初始化，生成一个初始化好的对象，拷贝给s6

    //string s(cp,n)
    char cs[]="12345";
    string s7(cs,3);//复制字符串cs的前3个字符到s当中

    //string s(s2,pos2)
    string s8="asac";
    string s9(s8,2);//从s2的第二个字符开始拷贝，不能超过s2的size

    //string s(s2,pos2,len2)
    string s10="qweqweqweq";
    string s11(s10,3,4);//s4是s3从下标3开始4个字符的拷贝，超过s3.size出现未定义
```
3. substr:

```c++
    string s="abcdefg";
//s.substr(pos1,n)返回字符串位置为pos1字符开始，n个字符组成的串
    string s2=s.substr(1,5);//bcdef

    //s.substr(pos)//得到一个pos到结尾的串
    string s3=s.substr(4);//efg
```
**4. insert:**
```c++
  string str="to be question";
    string str2="the ";
    string str3="or not to be";
    string::iterator it;

    //s.insert(pos,str)//在s的pos位置插入str
    str.insert(6,str2);                 // to be the question

    //s.insert(pos,str,a,n)在s的pos位置插入str中插入位置a到后面的n个字符
    str.insert(6,str3,3,4);             // to be not the question

    //s.insert(pos,cstr,n)//在pos位置插入cstr字符串从开始到后面的n个字符
    str.insert(10,"that is cool",8);    // to be not that is the question

    //s.insert(pos,cstr)在s的pos位置插入cstr
    str.insert(10,"to be ");            // to be not to be that is the question

    //s.insert(pos,n,ch)在s.pos位置上面插入n个ch
    str.insert(15,1,':');               // to be not to be: that is the question

    //s.insert(s.it,ch)在s的it指向位置前面插入一个字符ch，返回新插入的位置的迭代器
    it = str.insert(str.begin()+5,','); // to be, not to be: that is the question

    //s.insert(s.it,n,ch)//在s的it所指向位置的前面插入n个ch
    str.insert (str.end(),3,'.');       // to be, not to be: that is the question...

    //s.insert(it,str.ita,str.itb)在it所指向的位置的前面插入[ita,itb)的字符串
    str.insert (it+2,str3.begin(),str3.begin()+3); // to be, or not to be: that is the question...
```
**5. erase操作：**
用来执行删除操作
删除操作有三种

1. 指定pos和len，其中pos为为起始位置，pos以及后面len-1个字符串都删除
2. 迭代器，删除迭代器指向的字符
3. 迭代器范围，删除这一范围的字符串，范围左闭右开

```c++
                          // "This is an example sentence."
  str.erase (10,8);       //            ^^^^^^^^
  //直接指定删除的字符串位置第十个后面的8个字符
  std::cout << str << '\n';
                            // "This is an sentence."
  str.erase (str.begin()+9);//           ^
  //删除迭代器指向的字符
  std::cout << str << '\n';
                            // "This is a sentence."
                            //       ^^^^^
  str.erase (str.begin()+5, str.end()-9);
  //删除迭代器范围的字符
  std::cout << str << '\n';// "This sentence."

```
**6. append和replace操作:**

append函数可以用来在字符串的末尾追加字符和字符串。由于string重载了运算符，也可以用+=操作实现

repalce顾名思义，就是替换的意思，先删除，后增加。
```c++
// append:
 std::string str;
    std::string str2="Writing ";
    std::string str3="print 10 and then 5 more";

    //直接追加一个str2的字符串
    str.append(str2);                       // "Writing "
    //后面追加str3第6个字符开始的3个字符串
    str.append(str3,6,3);                   // "10 "
    //追加字符串形参的前5个字符
    str.append("dots are cool",5);          // "dots "
    //直接添加
    str.append("here: ");                   // "here: "
    //添加10个'.'
    str.append(10u,'.');                    // ".........."
    //添加str3迭代器范围的字符串
    str.append(str3.begin()+8,str3.end());  // " and then 5 more"
    //最后这个比较特殊，意思是添加5个'A'，实际上参数里面的65对应的asc码就是65
    str.append<int>(5,65);                // "....."
    //字符串追加也可以用重载运算符实现
    str+="lalala";
    std::cout << str << '\n';
```
**replace:**
```c++
// replace:
    std::string str="this is a test string.";
    std::string str2="n example";
    std::string str3="sample phrase";
    std::string str4="useful.";
//第9个字符以及后面的4个字符被str2代替
    str.replace(9,5,str2);          // "this is an example string." (1)
    //第19个字符串以及后面的5个字符用str的第7个字符以及后面的5个字符代替
    str.replace(19,6,str3,7,6);     // "this is an example phrase." (2)
    //第8个字符以及后面的9个字符用字符串参数代替
    str.replace(8,10,"just a");     // "this is just a phrase."     (3)
    //第8个字符以及后面的5个字符用字符串参数的前7个字符替换
    str.replace(8,6,"a shorty",7);  // "this is a short phrase."    (4)
    //第22以及后面的0个字符用3个叹号替换
    str.replace(22,1,3,'!');        // "this is a short phrase!!!"  (5)
    //迭代器的原理同上
    // Using iterators:                                               0123456789*123456789*
    str.replace(str.begin(),str.end()-3,str3);                    // "sample phrase!!!"      (1)
    str.replace(str.begin(),str.begin()+6,"replace");             // "replace phrase!!!"     (3)
    str.replace(str.begin()+8,str.begin()+14,"is coolness",7);    // "replace is cool!!!"    (4)
    str.replace(str.begin()+12,str.end()-4,4,'o');                // "replace is cooool!!!"  (5)
    str.replace(str.begin()+11,str.end(),str4.begin(),str4.end());// "replace is useful."    (6)

```
**7. assign操作：**

assign操作在一起列容器当中都存在，比如vector等等。是一个很基本的操作函数，string使用assign可以灵活的对其进行赋值。
```c++
    std::string str;
    std::string base="The quick brown fox jumps over a lazy dog.";

    // used in the same order as described above:
    //直接把base赋值给str
    str.assign(base);
    std::cout << str << '\n';
    //把base第10个字符以及后面的8个字符赋给str
    str.assign(base,10,9);
    std::cout << str << '\n';         // "brown fox"
    //把参数中的0到6个字符串赋给str
    str.assign("pangrams are cool",7);
    std::cout << str << '\n';         // "pangram"
    //直接使用参数赋值
    str.assign("c-string");
    std::cout << str << '\n';         // "c-string"
    //给str赋值10个'*'字符
    str.assign(10,'*');
    std::cout << str << '\n';         // "**********"
    //赋值是10个'-'
    str.assign<int>(10,0x2D);
    std::cout << str << '\n';         // "----------"
    //指定base迭代器范围的字符串
    str.assign(base.begin()+16,base.end()-12);
    std::cout << str << '\n';         // "fox jumps over"
```
8. string的搜索操作:


find和rfind函数:

find函数主要是查找一个字符串是否在调用的字符串中出现过，大小写敏感。

```c++
    std::string str ("There are two needles in this haystack with needles.");
    std::string str2 ("needle");

    // different member versions of find in the same order as above:
    //在str当中查找第一个出现的needle，找到则返回出现的位置，否则返回结尾
    std::size_t found = str.find(str2);
    if (found!=std::string::npos)
    std::cout << "first 'needle' found at: " << found << '\n';
    //在str当中，从第found+1的位置开始查找参数字符串的前6个字符
    found=str.find("needles are small",found+1,6);
    if (found!=std::string::npos)
    std::cout << "second 'needle' found at: " << found << '\n';
    //在str当中查找参数中的字符串
    found=str.find("haystack");
    if (found!=std::string::npos)
    std::cout << "'haystack' also found at: " << found << '\n';
    //查找一个字符
    found=str.find('.');
    if (found!=std::string::npos)
    std::cout << "Period found at: " << found << '\n';
    //组合使用，把str2用参数表中的字符串代替
    // let's replace the first needle:
    str.replace(str.find(str2),str2.length(),"preposition");

```

rfind函数就是找最后一个出现的匹配字符串，返回的位置仍然是从前往后数的。
```c++
std::string str ("The sixth sick sheik's sixth sheep's sick.");
    std::string key ("sixth");//                    ^
    //rfind是找最后一个出现的匹配字符串
    std::size_t found = str.rfind(key);
    if (found!=std::string::npos)
    {
        cout<<found<<endl;//输出23
        str.replace (found,key.length(),"seventh");//找到的sixth替换成seventh
    }
```

**3.find_….of函数:**
1. find_first_of(args) 查找args中任何一个字符第一次出现的位置
2. find_last_of(args) 最后一个出现的位置
3. find_fist_not_of(args) 查找第一个不在args中的字符
4. find_last_not_of 查找最后一个不在args中出现的字符
```c++
std::string str1 ("Please, replace the vowels in this sentence by asterisks.");
    std::size_t found1 = str1.find_first_of("aeiou");
    //把所有元音找出来用*代替
    while (found1!=std::string::npos)
    {
        str1[found1]='*';
        found1=str1.find_first_of("aeiou",found1+1);
    }
    std::cout << str1 << '\n';

    //在str2中找到第一个不是消协英文字母和空格的字符
    std::string str2 ("look for non-alphabetic characters...");
    std::size_t found2 = str2.find_first_not_of("abcdefghijklmnopqrstuvwxyz ");
    if (found2!=std::string::npos)
    {
        std::cout << "The first non-alphabetic character is " << str2[found2];
        std::cout << " at position " << found2 << '\n';
    }
```

**8. 比较与数值转化：**


如果两个字符串相等，那么返回0，调用对象大于参数返回1，小于返回-1。

string重载了运算符，可以直接用>,<，==来进行比较，也很方便

```c++
string s1="123",s2="123";
    cout<<s1.compare(s2)<<endl;//0

    s1="123",s2="1234";
    cout<<s1.compare(s2)<<endl;//-1

    s1="1234",s2="123";
    cout<<s1.compare(s2)<<endl;//1

    std::string str1 ("green apple");
    std::string str2 ("red apple");

    if (str1.compare(str2) != 0)
    std::cout << str1 << " is not " << str2 << '\n';
    //str1的第6个字符以及后面的4个字符和参数比较
    if (str1.compare(6,5,"apple") == 0)
    std::cout << "still, " << str1 << " is an apple\n";

    if (str2.compare(str2.size()-5,5,"apple") == 0)
    std::cout << "and " << str2 << " is also an apple\n";
    //str1的第6个字符以及后面的4个字符和str2的第4个字符以及后面的4个字符比较
    if (str1.compare(6,5,str2,4,5) == 0)
    std::cout << "therefore, both are apples\n";
```

**9 .数值转换：**[学习链接](https://blog.csdn.net/u010510020/article/details/73799996)

在io的部分有过数值和字符串相互转换的例子，使用的是stringstream函数，在c++11当中有定义好的现成的函数取调用，非常方便。

**一、int转string**

1.c++11标准增加了全局函数std::to_string:

string to_string (int val);

string to_string (long val);

string to_string (long long val);

string to_string (unsigned val);

string to_string (unsigned long val);

string to_string (unsigned long long val);

string to_string (float val);

string to_string (double val);

string to_string (long double val);

**二、string转int:**
```c++
 stoi(s,p,b); //int
 stol(s,p,b); // long
 stod() //double
 stof() // float
 stoul(s,p,b);// unsigned long
 stoll(s,p,b);// long l
 stoull(s,p,b); // u l l 
```
其中b表示转换所用的基数，默认为10(表示十进制).

p是size_t的指针，用来保存s中第一个非数值字符的下标，p默认为0，即函数不返 回下标.

**9.返回某一个char：**
str.at()

**10. 字符长度**
str.length()
str.size()

### 结构体初始化：

```c++
struct Person{
    char name[20];                       //姓名 
    int count;                           //计数器
};
int main(){
    Person leader[3]={"Tom",0,"Neo",0,"Marry",0};

struct A
{
	int b;
	int c;
}；
struct A a = {1, 2};

//点号+赋值符号
struct A a = {.b = 1, .c = 2};

//冒号
struct A a = {b:1, c:2};

//构造函数初始化常见于 C++ 代码中，因为 C++ 中的 struct 可以看作class，
//结构体也可以拥有构造函数，所以我们可以通过结构体的构造函数来初始化结构体对象。给定带有构造函数的结构体：
struct A 
{
	A(int a,int b)
	{
		this->a=a;
		this->b=b;
	};
	int b;
	int c;
}；
//那么结构体对象的初始化可以像类对象的初始化那样
struct A a(1,2);

//依次给每一个结构体成员变量进行赋值：
struct A a; 
a.b=1;
a.c=2;

```
**注意** `struct 如果定义了构造函数的话，就不能用大括号进行初始化了，即不能再使用指定初始化与顺序初始化了。`

初始化与赋值有着本质的区别，初始化是变量定义时的第一次赋值，赋值则是定义之后的值的变更操作，概念上不同，所以实现上也不一样

### 部分初始化：
```c++
struct Date
{
    int day, month, year;
};
```
也可以仅初始化结构体变量的部分成员。例如，如果仅知道要存储的生日是8月23日， 但不知道年份，则可以按以下方式定义和初始化变量：
Date birthday = {23,8};

这里只有 day 和 month 成员被初始化，year 成员未初始化。但是，如果某个结构成员未被初始化，则所有跟在它后面的成员都需要保留为未初始化。

使用初始化列表时，C++ 不提供跳过成员的方法。以下语句试图跳过 month 成员的初始化。这是不合法的。
Date birthday = {23,1983}; //非法

**使用构造函数来初始化结构体成员变量**，这和初始化类成员变量是相同的。与类构造函数一样，结构体的构造函数必须是与结构体名称相同的公共成员函数，并且没有返回类型。因为默认情况下，所有结构体成员都是公开的，所以不需要使用关键字 public
```c++
struct Employee
{
    string name;    // 员工姓名
    int vacationDays,    // 允许的年假
    daysUsed;    //已使用的年假天数
    // 使用构造函数和
    Employee (string n ="",int d = 0)    // 构造函数
    {
        name = n;
        vacationDays = 10;
        daysUsed = d;
    }
};
```