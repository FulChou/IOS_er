#include<iostream>
#include<string>
#include<cmath>
using namespace std;

// ascii 码中 ‘0’ 是48 要减去‘0’
int main(){
    string str;
    while(cin>>str){
        long sum = 0;
        for(int i=0;i<str.size();i++){
            sum+=(str[i]-'0') * (pow(2, str.size()-i)-1);
        }
        cout<<sum<<endl;
    }
    return 0 ;
}