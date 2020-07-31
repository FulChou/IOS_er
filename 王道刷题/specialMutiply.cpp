#include<iostream>
#include<string>

using namespace std;

int main(){
    string str1;
    string str2;
    int answer;
    while(cin>>str1>>str2){
        answer = 0;
        for(int i=0;i<str1.size();i++)
            for(int j=0;j<str2.size();j++){
                answer += (str1[i]-'0')*(str2[j]-'0');
            }
        cout<<answer<<endl;
    }
    return 0;
}