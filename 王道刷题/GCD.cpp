#include<iostream>
#include<cstdio>

using namespace std;

int GCD(int a,int b){
    if(!b){
        return a;
    }else return GCD(b, a%b);
}
int main(){
    
    int a,b;
    while(scanf("%d %d",&a,&b)!=EOF){
        cout<<GCD(a, b)<<endl;
    }
    
    return 0;
    
}