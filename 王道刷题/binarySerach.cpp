#include<iostream>
#include<algorithm>

using namespace std;

bool binarySearch(int n,int nums[],int target){
     int left,right,mid;
     //bool isFind = false;
     left=0;right=n-1;
     while(left<=right){ 
     mid = (left+right)/2;// every time mid need change
     if(target>nums[mid]){
     left = mid+1;
     }
     else if(target<nums[mid]){
     right = mid-1;  // ++  -- 对赋值语句没用，只改变当前的mid；
     }else{
            return true;
    }
        }    
    return false;
}

int main(){
    int n,m;
    while(cin>>n){
        int nums[n];
        for(int i=0;i<n;i++){
            cin>>nums[i];
        }
        cin>>m;
        int nFind[m];
        for(int i=0;i<m;i++){
            cin>>nFind[i];
        }
        sort(nums,nums+n);
        // 对于每个 element in nfindp[]
        for(int i=0;i<m;i++){
            if(binarySearch(n,nums,nFind[i])) cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
        
    }
    return 0;
}