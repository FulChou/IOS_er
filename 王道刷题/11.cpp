#include <iostream>
#include <cstdio>

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
    int time;
    int year,month,day,num;
    cin>>time;
    for(int i=0;i<time;i++){
        scanf("%d%d%d%d",&year,&month,&day,&num); //输入语法错误；中间没有逗号
        // printf("hello %d %d,%d,%d \n",year,month,day,num);
        for(int j=0;j<month-1;j++){
            num+=datas[isLeapYear(year)][j]; // 针对的是i的变化，也就是for里面的变量写错了；
        }
        num+=day; //calculate days

        while(num>numberOfYear(year)){  //
            num -= numberOfYear(year);
            year++;
        }
        month=0;//忘记归零；

        for(int k=0;k<12;k++){ // for里面选取的符号最好要不一样；
            if(num-datas[isLeapYear(year)][k]>0){
              num-=datas[isLeapYear(year)][k];
              month++;
            }else break;
        }
        month++;
        day=num;
        printf("%04d-%02d-%02d\n",year,month,day);
    }
    return 0;
}