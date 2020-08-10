#include<iostream>
#include<string>
#include<cctype> // 熟悉cctype

using namespace std;

int main(){
    string str;
    while(getline(cin, str)){
        if(str.size()>0){ //  时间3ms也还能接受，或者使用数组来存储 char 一个一个来判断是不是空格 和 是不是第一个 //逻辑是一样的
            for(int i=0;i<str.size();i++){
                if(i==0&&isalpha(str[i])) str[i] = toupper(str[i]);
                else if(isspace(str[i-1])&&isalpha(str[i]))str[i] = toupper(str[i]);
            }
            cout<<str;
        }
    }
    return 0;
}