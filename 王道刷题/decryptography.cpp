#include<iostream>
#include<string>

using namespace std;

int main(){
    string str;
    //int n;
    //while(cin>>n){
        while(getline(cin, str)){
        //n--;
        //getline(cin, str);
        for(int i=0;i<str.size();i++){
            // 两端循环来加1
            if((str[i]>='a'&&str[i]<='z')){
                str[i] = (str[i]-'a'+1)%26 + 'a';
            }
            else if((str[i]>='A'&&str[i]<='Z'))
            {   
                str[i] = (str[i]-'A'+1)%26+'A';
                
            }
            //else if(str[i]=='z'||str[i]=='Z') str[i]=str[i]-25;
        }
         cout<<str<<endl;
    }
    //}
    return 0;
}