#include<iostream>
#include<stack>

using namespace std;
// 不用真的堆栈，采用数组实现会更加快：
int main(){
    int n;
    while(cin>>n){
        if(n==0) break;
        char type;
        stack<int> s; // 放到 for循环之外初始化；
        for(int i=0;i<n;i++){
            cin>>type;
            if(type=='O'){
                if(!s.empty()) s.pop();
            }else if(type=='A'){
                if(s.size()==0){ //
                    cout<<"E"<<endl;
                } 
                else cout<<s.top()<<endl;
            }
            else if(type=='P'){
                int num;
                cin>>num;
                s.push(num);
                
            }
            
        }
        cout<<endl;
    }
    return 0;
}