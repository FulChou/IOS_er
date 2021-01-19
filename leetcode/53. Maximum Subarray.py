'''
Author: Ful Chou
Date: 2021-01-19 10:55:46
LastEditors: Ful Chou
LastEditTime: 2021-01-19 11:09:36
FilePath: /leetcode/53. Maximum Subarray.py
Description: What this document does
链接： https://leetcode-cn.com/problems/maximum-subarray/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        暴力 n^2 个 subarray
        dp: 方法
        dp[i] 以 nums[i] 结尾 最大的 subarray:
        dp[i] = max(dp[i-1], 0) + num[i]
        全靠自己想到动归解法，还是很有成就感的！
        节约空间 可以不需要 dp 数组
        '''
        n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = [0] * n
        # dp[0] = nums[0]
        for i in range(1, n):
            nums[i] = max(nums[i-1], 0) + nums[i]
        return max(nums)
