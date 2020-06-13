#include <iostream>
#include<cstdio>

using namespace std;

int main(){
    int n;
    while(scanf("%d",&n)!=EOF){
        int step=0;
        if(n==0) break;
        while(n!=1){
            if(n%2==0){
                n/=2;
            }else{
                n=(3*n+1)/2; // 注意看题！要除2；
            }
            step++;
        }
        printf("%d\n",step);
    }
    return 0;
}