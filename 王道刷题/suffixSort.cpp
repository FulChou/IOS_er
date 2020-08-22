#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

// bool cmp(string a,string b){
//     return a<b;
// }


int main(){
    string str;
    
    while(cin>>str){
        string strArry[str.size()] ;
        for(int i=0;i<str.size();i++){
            strArry[i] = str.substr(str.size()-1-i,i+1);
        }
        sort(strArry,strArry+str.size());
        for(int i=0;i<str.size();i++){
            cout<<strArry[i]<<endl;
        }
    }
    
    return 0;
}