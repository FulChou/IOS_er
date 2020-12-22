'''
Author: Ful Chou
Date: 2020-11-09 20:22:20
LastEditors: Ful Chou
LastEditTime: 2020-12-21 16:39:42
FilePath: /leetcode/house_robber.py
Description: What this document does
'''

### 198 house robber: 11.09 08:22

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        ### 这个是逆着 dp
        ### dp[i] = max(dp[i+1], dp[i+2] + nums[i]) 从 0到第i间 屋子偷窃的钱
        # max_table = [-1 for i in range(n)] # 记忆table
        # def dp(start:int, n:int):
        #     if start >= n:
        #         return 0
        #     elif max_table[start] != -1:
        #         return max_table[start]
        #     else:
        #         res = max(dp(start + 1, n), dp(start + 2, n) + nums[start])
        #         max_table[start] = res
        #         return res
        # return dp(0,n)

        ### 顺着的 dp：
        dp_i, dp_i1, dp_i2 = 0, 0, 0
        for i in range(n-1,-1,-1):
            dp_i = max(dp_i1 ,dp_i2 + nums[i])
            dp_i2 = dp_i1
            dp_i1 = dp_i
            # print(i,dp_i)
        return dp_i
    def rob(self, nums: List[int]) -> int:
        #  max profit is last house 
        """
        house[i] = max(house[i-1], house[i-2]+nums[i])
        两个月后自己写还是能做出来，可以的
        优化内存：不需要一个数组去存储中间结果，只需要记住前一个房子和前两个房子的结果
        """
        n = len(nums)
        if n==0:
            return 0
        housei, housei1, housei2 = 0, 0, 0
        for i in range(n):
            housei = max(housei1, housei2 + nums[i])
            housei2 = housei1 
            housei1 = housei
        return housei