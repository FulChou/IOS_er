#include<iostream>
#include<queue>
#include<string>
#include<stack>
using namespace std;
//  N (≤10^100). 扫描字符串，字符串加法：

string digits [10] = {"zero","one","two","three","four","five","six","seven","eight","nine"};

string stringAdd(string a,string b){
    string str;
    int index;
    if(a.size() >= b.size()){
        index = b.size();
    } 
    else {
        index = a.size();
    }
    int p = 0;
    for (int i = 0; i < index; i++)
    {
        int sum = p + a[a.size()-i-1] -'0' + b[b.size()-i-1] - '0';
        p = sum/10;
        int result = sum%10;
        str.insert(0,to_string(result));
    }// 如果加了刚好要进位呢？
    // 加到前面去。。

    if(a.size()>index){
        int bound = a.size()-index; // 剩下的数：
       for (int i = 0; i < bound; i++)
       {
           int sum = p + a[a.size()-i-1-index] -'0';
           int result = sum%10;
           p = sum/10;
           str.insert(0,to_string(result));
       }

    }
    if(b.size()>index){
        int bound = b.size()-index; // 剩下的数：
       for (int i = 0; i < bound; i++)
       {
           int sum = p + b[b.size()-i-1 -index] -'0';
           int result = sum%10;
           p = sum/10;
           str.insert(0,to_string(result));
       }
    }

    if(p>0){
        str.insert(str.begin(),'1');
    }
    return str;
}

int main(){
    string n ;
    string sum = "0";
    cin>>n;

    for(int i=0;i<n.size();i++){
        sum = stringAdd(sum ,n.substr(i,1));
        //cout<<sum<<"next:"<<n.substr(i,1)<<" size"<<sum.size()<<endl;
    }
    bool flag = true;
    for (int i = 0; i < sum.size(); i++)
    {   
        //cout<< sum[i]<<":"<<digits[sum[i]];
        if (flag){
            cout<<digits[sum[i]-'0']; //to int
            flag = false;
        } 
        else  cout<<" "<<digits[sum[i] - '0'];
    }
    return 0;
}
//  123456789


/*
1005 Spell It Right (20分)
Given a non-negative integer N, your task is to compute the sum of all the digits of N, and output every digit of the sum in English.

Input Specification:
Each input file contains one test case. Each case occupies one line which contains an N (≤10
​100
​​ ).

Output Specification:
For each test case, output in one line the digits of the sum in English words. There must be one space between two consecutive words, but no extra space at the end of a line.

Sample Input:
12345
Sample Output:
one five

*/