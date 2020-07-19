#include<iostream>
#include<cstdio>

using namespace std;
// 理解错 题意了。
int main(){
    int n;
    int a1,a2,a3,b1,b2,b3;
    scanf("%d",&n);
    while (n>0)
    {
        n--;
        int sum=0;
        scanf("%d %d %d %d %d %d",&a1,&a2,&a3,&b1,&b2,&b3);
        // 最少：
        sum += b1+b2+b3;
        int leastB = 3*b1+2*b2+1*b3;
        int sumA= a1*1+a2*2+a3*3;
        if(sumA>leastB){
             if((sumA-leastB)%4==0){
                sum += (sumA-leastB)/4;
            }else
            {
                sum += (sumA-leastB)/4+1;
            }
        }
        printf("%d\n",sum);
    }
    return 0;
}