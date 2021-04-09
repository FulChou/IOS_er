'''
Author: Ful Chou
Date: 2021-04-09 10:52:18
LastEditors: Ful Chou
LastEditTime: 2021-04-09 10:52:31
FilePath: /leetcode/154. Find Minimum in Rotated Sorted Array II.py
Description: What this document does
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        nums_min = float('inf')
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                nums_min = min(
                    nums[left],
                    nums_min,
                )
                left = left + 1 # 我自己采用左侧逼近：
                # right = right - 1
                # 这样既不担心左侧出现最小值（即不需要使用min)， 也不用担心没有进入下一步
                # return nums[right]
        return nums_min