#include <iostream>
#include "stdio.h"
using namespace std;
// 暴力破解第一题：
int main(){
    for(int a=0;a<=9;a++)
        for(int b=0;b<=9;b++)
            for(int c=0;c<=9;c++){
                if(a*100+b*10+c+b*100+c*10+c==532)
                    printf("%d %d %d",a,b,c);
            }
    return 0;
}