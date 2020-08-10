#include<iostream>
#include<string>

using namespace std;



int main(){
    string s,a,b;
    while(getline(cin,s)){
        if(s.size()>0){
            cin>>a>>b;
            for(int i=0;i<s.size()-a.size()+1;i++){
            if(s[i]==a[0]&&s.substr(i,a.size())==a){ // 判断一个开头，这样节约了时间
                if(i>0&&i<s.size()-a.size()&&s[i-1]==' '&&s[i+a.size()]==' ') s.replace(i,a.size(),b); // 判断中间的word
                else if(i==0&&s[i+a.size()]==' ') s.replace(i,a.size(),b); // 开始的word
                else if(i==s.size()-a.size()&&s[i-1]==' ') s.replace(i,a.size(),b); // 最后的word
            }
        }
            cout<<s<<endl;
        }

    }
    return 0;
}