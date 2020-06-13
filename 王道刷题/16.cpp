#include <iostream>
#include <cstdio>

using namespace std;
int datas[2][12]={{31,28,31,30,31,30,31,31,30,31,30,31},
                  {31,29,31,30,31,30,31,31,30,31,30,31}};
int isLeapYear(int year){
    return (year%4==0&&year%100!=0)||year%400==0;
}
//  日期类，加一天操作；
int main(){
    int n;
    scanf("%d",&n);
    while(n>0){
        n--;
    int year,month,day;
    scanf("%d%d%d",&year,&month,&day);
    day++;
    if(day>datas[isLeapYear(year)][month-1]){
        day=1;
        month++;
        if(month>12){
            month=1;
            year++;
        }
    }
    printf("%04d-%02d-%02d\n",year,month,day);
    }
    return 0;
    
}