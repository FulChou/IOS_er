#include <iostream>

using namespace std;

bool is7Num(int x){
    if(x%7==0)
            return false;
    while(x!=0){
        if(x%10==7)
            return false;
        x /= 10;
    }
    return true;
}

int main(){
    int result = 0;
    int n;
    cin>>n;
    for(int i=0;i<=n;i++){
        if(is7Num(i))
            result+=i*i;
    }
    printf("%d",result);
    return 0;
}