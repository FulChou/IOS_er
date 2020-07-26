#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int n;
    while (cin>>n)
    {
        int nums[n];
        int max = 0;
        for(int i=0;i<n;i++){
            cin>>nums[i];
            if(nums[i]>max)
            max = nums[i];
        }
        cout<<max<<endl;
        sort(nums,nums+n);
        if(n==1) cout<<-1;
        else
        {
            for(int i=0;i<n-1;i++){
            cout<<nums[i]<<" ";
            }
        }
    }
    
    return 0;
}