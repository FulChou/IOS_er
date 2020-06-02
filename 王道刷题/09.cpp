#include<iostream>
#include<stdio.h>

using namespace std;

// 预处理：
int datas[2][12]={{31,28,31,30,31,30,31,31,30,31,30,31},
                  {31,29,31,30,31,30,31,31,30,31,30,31}};
int isLeapYear(int year){
    return ((year%400==0)||((year%4==0)&&(year%100!=0)));
}

int main(){
    int year,month,day;
    
    while(scanf("%d%d%d",&year,&month,&day)!=EOF){
        int num=0;
        int row=isLeapYear(year);// calculate year
        for(int i=0;i<month-1;i++){ // month-1
            num+=datas[row][i];
        }
        num+=day;
        printf("%d\n",num); // 转译符号是左上到右下；
    }
    return 0;
}