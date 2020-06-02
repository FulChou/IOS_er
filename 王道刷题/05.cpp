#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int n,x,y,z,a,b;
    bool flag=false;
    while(cin>>n>>x>>y>>z){
        for(int a=9;a>0;a--){// 循环的结束条件一定要多次确认
            for(int b=9;b>=0;b--){
                if((a*10000+x*1000+y*100+z*10+b)% n==0){
                    flag=true;
                    printf("%d %d %d \n",a,b,(a*10000+x*1000+y*100+z*10+b)/n);
                    break; // 找到了最佳答案之后，如何退出多重循环；
                }
            }
            if(flag) break;
        }
        if(!flag){
              printf("%d\n",0);
        }
    }
    return 0;
}