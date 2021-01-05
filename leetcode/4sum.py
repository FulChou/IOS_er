'''
Author: Ful Chou
Date: 2021-01-05 16:48:01
LastEditors: Ful Chou
LastEditTime: 2021-01-05 18:47:10
FilePath: /leetcode/4sum.py
Description: What this document does
链接：https://leetcode-cn.com/problems/4sum/submissions/
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        利用三数之和来做四数之和，思路一样：
        然而 三数之和 也是利用了 二数之和
        所以 我这里直接写一个 nSum 的解法来做这个题目了:
        '''
        n = len(nums)
        if n < 3: return []
        nums.sort()
        begin = 0
        return self.nSumTarget(4,begin,nums,target)

    def nSumTarget(self,n,begin,nums,target):
        nums_size = len(nums)
        res = []
        if n < 2 or nums_size < n: # 少于2数，少于n的数组 直接返回
            return res
        if n == 2:
            left = begin
            right = nums_size - 1
            while left < right:
                two_sum = nums[left] + nums[right] #放循环里面计算，避免 out of index
                if two_sum > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif two_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif two_sum == target:
                    res.append([nums[left],nums[right]])
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            return res
        else:
            for idx in range(begin,nums_size):
                if idx > begin and nums[idx] == nums[idx-1]: # 去掉后续重复的选择 同一个数
                    continue
                remain = target - nums[idx]
                nSums = self.nSumTarget(n - 1,idx + 1,nums,remain) # n-1, begin+1
                for nSum in nSums:
                    nSum.append(nums[idx])
                    res.append(nSum)
            return res