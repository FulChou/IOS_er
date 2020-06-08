#include <iostream>
#include <cstdio>
#include <string>
#include <math.h>

using namespace std;

int datas[2][12]={{31,28,31,30,31,30,31,31,30,31,30,31},
                  {31,29,31,30,31,30,31,31,30,31,30,31}};
int isLeapYear(int year){
    return (year%4==0&&year%100!=0)||year%400==0;
}
int numberOfYear(int year){
    if(isLeapYear(year)) 
        return 366;
    else 
        return 365;
}

int main(){
    string time1;
    string time2;
    int year,month,day,year2,month2,day2;
    while(getline(cin,time1)&&getline(cin,time2)){
        int num=1;
        int flag = time1.compare(time2);
        year=stoi(time1.substr(0,4)); // substr 的使用，是从index开始，数n个字符组成的字符串。index--(index+n-1)
        year2=stoi(time2.substr(0,4));
        month=stoi(time1.substr(4,2));
        month2=stoi(time2.substr(4,2));
        day=stoi(time1.substr(6,2));
        day2=stoi(time2.substr(6,2));
        
        int numOfYear=abs(year-year2);
        
        int num1,num2;
        num1=num2=0;
        for(int i=0;i<month-1;i++){
            num1+=datas[isLeapYear(year)][i];
        }
        num1+=day;
         for(int i=0;i<month2-1;i++){
            num2+=datas[isLeapYear(year2)][i];
        }
        num2+=day2;
        if(flag>0){// first is biger
            while(numOfYear>0){
                num+=numberOfYear(year);
                year--;
                numOfYear--;
            }
            num+=(num1-num2);
        }else{
             while(numOfYear>0){
                num+=numberOfYear(year);
                year++;
                numOfYear--;
            }
            num+=(num2-num1);
        }
        printf("%d\n",num);
    }
    
    return 0;
}

//优秀答案：

// #include<stdio.h>
// #define leap(x) (x%400==0||(x%4==0&&x%100!=0)?1:0)
// #define Abs(x) ((x)>0?(x):-(x))
// typedef struct date
// {
//     int y, m, d;
// }Date;

// const int yd[2][13]={{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
//                      {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}};
                      
// int days(Date x)
// {
//     int sum=0, i;
//     int y=x.y, m=x.m, d=x.d;
//     for(i=0; i<y; i++)
//     {
//         if(leap(i))
//         {
//             sum+=366;
//         }
//         else
//         {
//             sum+=365;
//         }
//     }
//     for(i=1; i<m; i++)
//     {
//         sum+=yd[leap(y)][i];
//     }
//     sum+=d;
//     return sum;
// }
// int main(void)
// {
//     Date a, b;
//     while(scanf("%4d%2d%2d", &a.y, &a.m, &a.d)!=EOF) //读取固定的格式数据：
//     {
//         scanf("%4d%2d%2d", &b.y, &b.m, &b.d);
//         printf("%d\n", Abs(days(a)-days(b))+1);
//     }
//     return 0;
// }