#include<iostream>
#include<algorithm>

using namespace std;

int num[600];
int GCD(int a,int b){
    if(b==0){
        return a;
    }else return GCD(b, a%b);
}

int main(){
    int n;
    while(cin>>n){
    if (!n) break;
    for(int i=0;i<n;i++){
        cin>>num[i];
    }
    sort(num,num+n);
    int count=0;
    // 双重循环 太慢了。。。
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(GCD(num[i], num[j])==1){
                count++;
            }
        }
    }
    cout<<count<<endl;
    }
   
    
}