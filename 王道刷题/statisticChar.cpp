#include<iostream>
#include<string>

using namespace std;

int number[128];
int main(){
    string str1;
    string str2;
    while(getline(cin,str1)){
        if(str1 == "#") break;
        memset(number,0,sizeof(number));// or use for to reset number
        getline(cin, str2);
        for(int i=0;i<str2.size();i++){
            number[str2[i]]++;
        }
        for(int i=0;i<str1.size();i++){
            cout<<str1[i]<<" "<<number[str1[i]]<<endl;
        }
    }
    
    return 0;
}