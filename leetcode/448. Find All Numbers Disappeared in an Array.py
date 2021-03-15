'''
Author: Ful Chou
Date: 2021-02-13 19:47:42
LastEditors: Ful Chou
LastEditTime: 2021-02-13 19:48:07
FilePath: /leetcode/448. Find All Numbers Disappeared in an Array.py
Description: What this document does
448
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ### 低级办法：
        ### 用一个 n 数组，记录已经出现的元素， 没出现的元素值为0. 但是这样 需要额外的空间 O(n)。 不过python 在leecode 运行速度还挺快
        ### 不使用额外的空间：
        n = len(nums)
        for i in range(n):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i])-1])
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
        
