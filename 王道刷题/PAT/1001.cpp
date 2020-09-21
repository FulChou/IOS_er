#include<iostream>
#include<string>

using namespace std;

typedef long long ll;
ll a,b,result;

string format(int result){
    string str = to_string(result);
    if(str.size()>=4){
        int time;
        // calculate the num of commas:
        if(result>0){

            time = str.size()/3;
            if(str.size()%3==0) time--; 
        }
        else
        {
            time = (str.size()-1)/3;
            if((str.size()-1)%3==0) time--;
        }
        //cout<<time<<endl;
        // insert commas:
        for(int i=0;i<time;i++){
            str.insert(str.size() - (i+1)*3 -i,",");
            // str.insert(str.size()-i*3,',');
        }
        
    }
    return str;
}
int main(){
    cin>>a>>b;
    result = a+b;
    cout<<format(result);
    return 0;
}
/*
test case :
-2,000,000

1000000  1000000

*/
