#include<iostream>
#include<string>
#include<vector>

using namespace std;

string StrDivide(string str,int x){
    int rmd = 0;
    for(int i=0;i<str.size();i++){
        int result = rmd*10 + str[i]-'0';
        str[i] = result/x + '0';
        rmd = result%x;
    }
    int index = 0;
    while(!(str[index]-'0')){ // 不是等于数值0 ，是字符0
        index++;
    }
    return str.substr(index);
}

int main(){
    string str;
    
    while(cin>>str){
       // cout<<str;
        vector<int> binary;
        while(!str.empty()){
            int last = str[str.size()-1]-'0';
           // cout<<last;
            binary.push_back(last%2);
            str = StrDivide(str, 2);
        }
        for(int i=binary.size()-1;i>=0;i--){
            cout<<binary[i];
        }
        cout<<endl;
    }
}