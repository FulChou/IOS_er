'''
Author: Ful Chou
Date: 2021-04-08 11:20:49
LastEditors: Ful Chou
LastEditTime: 2021-04-08 11:20:56
FilePath: /leetcode/153. Find Minimum in Rotated Sorted Array.py
Description: What this document does
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2 : return nums[0]
        left,right = 0, n-1
        # min_num = float('inf')
        if nums[left] < nums[right]: return nums[left]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]: # 忽略右半部分
                right = mid
            else: 
                left = mid + 1 #导致 left 不是最小值所在， 两个升序序列！
        return nums[right]
        # return min(nums) # lc 只能学个思想，这个内置函数甚至比我二分还快 ！！