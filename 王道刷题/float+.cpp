#include<iostream>
#include<string>
using namespace std;
int flag = 0; // 标识位，是否要进位；
// 优化一下

string mergeLow0(string a,string b){// 计算小数位算法
    string c=" ";
    if(a.size()!=b.size()){
        int Minsize = a.size()>b.size()?b.size():a.size();
    if(a.size()>Minsize){

        c.insert(0,a.substr(Minsize,a.size()-Minsize)); //并不能优化很多。。。
        a.erase(Minsize,a.size()-Minsize);
        // while (a.size()>Minsize)
        // {
        //      c.insert(0,1,a[a.size()-1]);
        //      a.erase(a.size()-1,1);
        // }

    }
    else{
        c.insert(0,b.substr(Minsize,b.size()-Minsize));
        b.erase(Minsize,b.size()-Minsize);

        //         while (b.size()>Minsize)
        // {
        //      c.insert(0,1,b[b.size()-1]);
        //      b.erase(b.size()-1,1);
        // }
        }
    }
    while(!a.empty()&&!b.empty()){
        char x1 = a[a.size()-1];
        a.erase(a.size()-1, 1);
        char x2 = b[b.size()-1];
        b.erase(b.size()-1,1);
        int temp = (x1-'0')+(x2-'0');
        temp += flag;
        flag = temp/10;
        temp = temp%10;
        c.insert(0, to_string(temp));
    }
    c.erase(c.end()-1);
    return c;
}

string merge(string a,string b){ // 计算整数位算法：
    string c=" ";
    while(!a.empty()&&!b.empty()){
        char x1 = a[a.size()-1];
        a.erase(a.size()-1, 1);
        char x2 = b[b.size()-1];
        b.erase(b.size()-1,1);
        int temp = (x1-'0')+(x2-'0');
        temp += flag;
        flag = temp/10;
        temp = temp%10;
        //cout<<temp<<endl;
        c.insert(0, to_string(temp));
    }
    while(!a.empty()){
        char x1 = a[a.size()-1];
        a.erase(a.size()-1, 1);
        int temp = (x1-'0')+flag;
        flag = temp/10;
        temp = temp%10;
        c.insert(0, to_string(temp));
    }
    while(!b.empty()){
        char x1 = b[b.size()-1];
        b.erase(b.size()-1, 1);
        int temp = (x1-'0')+flag;
        flag = temp/10;
        temp = temp%10;
        c.insert(0, to_string(temp));
    }
    c.erase(c.end()-1);
    return c;
}


int main(){
    string str1,str2,str_int1,str_int2,str_float1,str_float2;
    // 输入数据
    getline(cin,str1);
    getline(cin,str2);

    // 区分出整数位和小数位：
    for(int i=0;i<str1.size();i++){
        if(str1[i]=='.'){ // 找到小数点位置：
            str_int1 = str1.substr(0,i);
            str_float1 = str1.substr(i+1);
            break;
        }
    }

    for(int i=0;i<str2.size();i++){
        if(str2[i]=='.'){ // 找到小数点位置：
            str_int2 = str2.substr(0,i);
            str_float2 = str2.substr(i+1);
            break;
        }
    }
    string low = mergeLow0(str_float1,str_float2); // 计算小数位
    string high = merge(str_int1,str_int2); // 计算整数位
    // 合并
    high = high + "."+ low;
    
    cout<<high<<endl;
}