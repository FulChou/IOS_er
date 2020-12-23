'''
Author: Ful Chou
Date: 2020-11-10 15:51:49
LastEditors: Ful Chou
LastEditTime: 2020-12-23 11:50:58
FilePath: /leetcode/Houser_robber2.py
Description: What this document does
'''
### 213 题 2020.12.23日 第二次做
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 : return 0
        if n == 1 : return nums[0]
        def dp(start,end):
            cur, pre = 0,0
            for i in range(start,end):
                pre, cur =  cur, max(cur, pre + nums[i])
            return cur
        return max(dp(0,n-1), dp(1,n)) # 拆分为两个线性问题