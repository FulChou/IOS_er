#include <iostream>
#include "stdio.h"

using namespace std;

// 依旧是采用暴力：
int main(){
    for(int a=1;a<=9;a++)
        for(int b=0;b<=9;b++)
            for(int c=0;c<=9;c++)
                for(int d=0;d<=9;d++){
                    //if(a!=0){ //注意不能让 a=0，不然就不是四位数了，而且全为0也是一个组合；
                    // 或者应该a从1开始遍历啊。
                    if((a*1000+b*100+c*10+d)*9==(d*1000+c*100+b*10+a)){
                        printf("%d \n",a*1000+b*100+c*10+d);
                    }
                    //}
                    
                }
    return 0;
}