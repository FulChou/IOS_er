#include<iostream>
#include<cstdio>

using namespace std;
//隐藏条件就是1年1月1日是星期一，把这个时间点设为锚点
// 字符串要用二维数组保存

char weeks[7][20]={"Sunday","Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
char months[12][20]={"January", "February", "March", "April", "May", "June", "July",
                    "August", "September", "October", "November", "December"};

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

bool isSameArray(char x[],char y[]){
    for(int i=0;i<20;i++){
        if(x[i]!=y[i])
            return false;
    }
    return true;
}
int day;
char month[20];
int year;


int main(){
    while(scanf("%d%s%d",&day,&month,&year)!=EOF){
        int num =0;
        // 计算月份的天数
        int monthNum=0;
        for(int i=0;i<12;i++){
            // if(months[i]==month){ // 不能直接判断字符数组，那样判断的是内存地址；
            //     monthNum=i;
            // }
            if(isSameArray(months[i],month))
            monthNum=i;// no add 1;
        }
       for(int i=0;i<monthNum;i++){
            num+=datas[isLeapYear(year)][i];
        }
        year--;
        while(year>0){
            num+=numberOfYear(year);
            year--;
        }
        num+=day;
        num=num%7;
        printf("%s\n",weeks[num]);
    }
    return 0;
}
