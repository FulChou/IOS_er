class Solution {
public:
    // vector<int> twoSum(vector<int>& nums, int target) {
    //     int index1,index2;
    //     vector<int> result;
    //     index1=index2 = 0;
    //     for(int i=0;i<nums.size();i++){
    //         for(int j=i+1;j<nums.size();j++){
    //             if(nums[i]+nums[j]==target){
    //                 // index1 = i;
    //                 // index2 = j;
    //                 result.push_back(i);
    //                 result.push_back(j);
    //                 break;
    //             }
    //         }
    //     }
    //     return result;
    // }
        vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m;
            
        vector<int> result;
        for(int i=0;i<nums.size();i++){
            m[nums[i]] = i;// key is 数字；
        }
            
        for(int i=0;i<nums.size();i++){
           int complement = target - nums[i];
            if(m.count(complement) && m[complement] != i){
                result.push_back(i);
                result.push_back(m[complement]);
                break;
                }
            }
  
        return result;
    }
    
};
