#include <iostream>
#include <cstdio>

using namespace std;

const int maxLine = 10000;
bool line[maxLine];

int L,M;

int main(){
    while(scanf("%d%d",&L,&M)!=EOF){
        int sum=L+1;
        for(int i=0;i<L+1;i++){
            line[i] = true;
        }
        while(M>0){
            M--;
            int left,right;
            scanf("%d %d",&left,&right); // 别忘记了&
            for(int i=left;i<=right;i++){// 可以用等于号，或者加一
                if(line[i]){
                    line[i]=false;
                    sum--;
                }
            }
        }
        printf("%d\n",sum);
    }
    return 0;
}