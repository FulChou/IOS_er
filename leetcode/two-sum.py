'''
Author: Ful Chou
Date: 2021-01-03 00:29:28
LastEditors: Ful Chou
LastEditTime: 2021-01-03 00:30:13
FilePath: /leetcode/two-sum.py
Description: What this document does

简单题不多说，空间换时间 链接： https://leetcode-cn.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # from collections import defaultdict
        '''
        哈希表 加快 find 速度
        '''
        dic = {} 
        for idx,num in enumerate(nums):
            dic[num] = idx
        for idx,num in enumerate(nums):
            res = target - num
            if res in dic and dic[res] != idx:
                return [idx, dic[res]]
        return [-1,-1]
