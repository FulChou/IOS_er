#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    int num[10];
    vector<int> even;
    vector<int> odd;
    while (cin>>num[0]>>num[1]>>num[2]>>num[3]>>num[4]>>num[5]>>num[6]>>num[7]>>num[8]>>num[9])
    {   // judge the odd ro even;
       for(int i=0;i<10;i++){
           if(num[i]%2==0)
            even.push_back(num[i]);
            else odd.push_back(num[i]);
       }
       sort(odd.begin(),odd.end(),greater<int>());
       sort(even.begin(),even.end());
       for (int i = 0; i < odd.size(); i++)
       {
           cout<<odd.at(i)<<" ";
       }
       for (int i = 0; i < even.size(); i++)
       {
           cout<<even.at(i)<<" ";
       }
    }
    
    return 0;
}