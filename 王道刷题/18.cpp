#include<iostream>
#include<cstdio>
#include"math.h"// 头文件 or <math.h>

using namespace std;

int main(){
    int P,T,G1,G2,G3,GJ;
    while(scanf("%d %d %d %d %d %d",&P,&T,&G1,&G2,&G3,&GJ)!=EOF){
        int d1,d2;
        double result;
        d1=abs(G1-G2);
        if(d1<=T) result=(double)(G1+G2)/2;
        else{
            d1=abs(G3-G1);
            d2=abs(G3-G2);
            // 一个内，一个外：
            if(d1<=T||d2<=T&&!(d1<=T&&d2<=T)){
                if(d1<=d2) result = (double)(G1+G3)/2;
                else result = (double) (G2+G3)/2;
            }
            // outside
            if(d1>T&&d2>T) result = GJ;
            // inside
            if(d1<=T&&d2<=T){
                if(G1-G2>0){
                    result = G1; 
                }else result=G2;
                if(result-G3<0) result = G3;
            }
        }
        printf("%.1f\n",result);
        
    }
    return 0;
}