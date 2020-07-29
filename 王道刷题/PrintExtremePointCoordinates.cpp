#include<iostream>

using namespace std;

bool isMaxOrMin(int n,int nums[],int index){
    bool result=false;
    if(index==0){
        if(nums[index+1]!=nums[index]) result = true;
        
    }else if(index==n-1){
        if(nums[index-1]!=nums[index]) result = true;
    }else{
        if((nums[index]>nums[index+1]&&nums[index]>nums[index-1])||
           (nums[index]<nums[index+1]&&nums[index]<nums[index-1]))
            result = true;
    }
    return result;
}

int main(){
    int k;
    while(cin>>k){
        int nums[k];
        for(int i=0;i<k;i++){
            cin>>nums[i];
        }
        for(int i=0;i<k;i++){
            if(isMaxOrMin(k, nums, i))
                cout<<i<<" "; // 输出坐标：
        }
        cout<<endl;
        
    }
    return 0;
}