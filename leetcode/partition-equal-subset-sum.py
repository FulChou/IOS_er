'''
Author: Ful Chou
Date: 2021-01-12 20:23:34
LastEditors: Ful Chou
LastEditTime: 2021-01-12 20:24:21
FilePath: /leetcode/partition-equal-subset-sum.py
Description: What this document does
链接： https://leetcode-cn.com/problems/partition-equal-subset-sum/
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        官方dp： 0，1背包问题变式
        第一版：
        i: 0 ~ n-1 
        w: 0 ~ target
        dp[i][w] = dp[i-1][w] or dp[i-1][w - num[i]]
        dp[0][...] = False
        dp[...][0] = True
        第二版: 
        优化内存占用 ：
        只需要前一天的各种 w 状态:
        dp[w]： 0 ~ targe 
        dp[i][w] = dp[i-1][w] or dp[i-1][w - num[i]]
        需要注意的是第二层的循环我们需要从大到小计算，
        因为如果我们从小到大更新 dp 值，那么在计算 dp[w] 值的时候， 
        dp[w − nums[i]] 已经是被更新过的状态，不再是上一 行的 dp 值
        '''
        # n = len(nums)
        # list_sum = sum(nums)
        # if list_sum % 2 != 0:
        #     return False
        # target = list_sum // 2
        # dp = [[False for i in range(target+1)] for j in range(n+1)]
        # for i_list in dp:
        #     i_list[0] = True
        # for i in range(1,n+1):
        #     for w in range(1,target+1):
        #         if w - nums[i-1] < 0:
        #             dp[i][w] = dp[i-1][w]
        #         else:
        #             dp[i][w] = dp[i-1][w] or dp[i-1][w - nums[i-1]]
        # return dp[n][target]
######## 压缩 状态空间 的实现 ################
        n = len(nums)
        list_sum = sum(nums)
        if list_sum % 2 != 0:
            return False
        target = list_sum // 2
        dp = [False for i in range(target+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in range(target,0,-1): # 倒序，从大到小：
                if w - nums[i-1] >= 0:
                    dp[w] =  dp[w] or dp[w - nums[i-1]]
        return dp[target]