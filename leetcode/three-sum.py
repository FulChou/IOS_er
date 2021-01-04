'''
Author: Ful Chou
Date: 2021-01-04 20:47:00
LastEditors: Ful Chou
LastEditTime: 2021-01-04 20:47:23
FilePath: /leetcode/three-sum.py
Description: What this document does
链接：https://leetcode-cn.com/problems/3sum/submissions/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        思路就是
        1. 先将数组排序，从左到右循环取一个数，用 target 也就是0 去减 这个数 得到结果 remain
        2. remain 的值就是 另外两数之和的结果，而且是比第一个数大的两数之和。所以将remain 放到两数之和进行计算即可得到结果
        '''
        n = len(nums)
        if n < 3:
            return []
        target = 0
        nums.sort()
        res = []
        for idx,num in enumerate(nums):
            if num > 0: return res # tip: 加速程序运行，从小到大取值，第一个数大于0，之后不可能有和为0的情况。
            if idx >= 1 and num == nums[idx-1]:
                continue
            remain = target - num
            tree_sums = self.twoSumTarget(nums,remain,idx)
            for tree_sum in tree_sums:
                tree_sum.append(num)
                res.append(tree_sum)
        return res

    def twoSumTarget(self,nums,target,begin):
        res = []
        left = begin+1 # 从右边的第一位开始 算two_sum
        right = len(nums) - 1
        while left < right:
            twosum = nums[left] + nums[right]
            if twosum > target:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -=1
            elif twosum < target:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left +=1
            elif twosum == target:
                res.append([nums[left],nums[right]])
                # 左右移动一位：
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -=1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left +=1
        return res
