#include<iostream>
#include<string>
#include<cstdio>

using namespace std;


int keytab[26]={1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4};
// 手机键盘：
int main(){
    string str;
    while(cin>>str){
        int time=0;
        for(int i=0;i<str.size();i++){
            time+=keytab[str[i]-'a']; // 写错了；str...
            if(i!=0&&str[i]-str[i-1]==keytab[str[i]-'a']-keytab[str[i-1]-'a']) // 如果是同一个键盘，那么点击次数的差就是他们之间的距离；
                time+=2;
        }
            printf("%d\n",time);
    }
    return 0;
}