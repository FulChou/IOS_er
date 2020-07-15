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
    int N;
    scanf("%d",&N);
    string time1;
    string time2;
    int year,month,day,year2,month2,day2;
    while(N>0){
        N--;
        scanf("%4d-%2d-%2d %4d-%2d-%2d", &year, &month, &day, &year2, &month2, &day2);
        int num=1;
        int flag = time1.compare(time2);
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