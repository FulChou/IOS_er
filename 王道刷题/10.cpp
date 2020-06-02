#include<iostream>
#include<stdio.h>

using namespace std;


int datas[2][12]={{31,28,31,30,31,30,31,31,30,31,30,31},
                  {31,29,31,30,31,30,31,31,30,31,30,31}};
int isLeapYear(int year){
    return ((year%400==0)||((year%4==0)&&(year%100!=0)));
}

int main(){
    int year,num;
    
    while(scanf("%d%d",&year,&num)!=EOF){
        int month=0;
        int day = 0;
        int row=isLeapYear(year);// calculate year
        
        for(int i=0;i<12;i++){ 
            if(num-datas[row][i]<0){
                break;
            }
            num-=datas[row][i];
            month++; // 虽然只过了11个整日子，但是要叫12月！！！
        }
        month++;
        day = num;
        printf("%04d-%02d-%02d",year,month,day); // 处理输出知识点：
    }
    return 0;
}
