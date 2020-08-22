#include<iostream>
#include<stack>

using namespace std;
int main(){
    
    unsigned int num;
    while(cin>>num){
        stack<int> binary;
        while(num!=0){
            binary.push(num%2);
            num/=2;
        }
        while(!binary.empty()){
            cout<<binary.top();
            binary.pop();
        }
        cout<<endl;
    }
    return 0;
}