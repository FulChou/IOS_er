'''
Author: Ful Chou
Date: 2021-04-05 14:12:12
LastEditors: Ful Chou
LastEditTime: 2021-04-05 14:12:13
FilePath: /leetcode/88. Merge Sorted Array.py
Description: What this document does
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 使用 额外的排序时间O(nlogn) 空间也要 log n 的就不写了，太捞了
        # # 使用了 额外的空间 O(m+n)
        # temp = [0] * (m+n)
        # idx1 = 0
        # idx2 = 0
        # idex = 0
        # while idx1 < m and idx2 < n:
        #     if nums1[idx1] <= nums2[idx2]:
        #         temp[idex] = nums1[idx1] # 使用 append 不开心吗？
        #         idx1 += 1
        #     else:
        #         temp[idex] = nums2[idx2]
        #         idx2 += 1
        #     idex += 1
        # while idx1 < m:
        #     temp[idex] = nums1[idx1]
        #     idx1 += 1
        #     idex += 1
        # while idx2 < n:
        #     temp[idex] = nums2[idx2]
        #     idx2 += 1
        #     idex += 1
        # for i in range(n+m):
        #     nums1[i] = temp[i]
        # 不需要 额外空间的 方法  即从倒序双指针：
        idx1, idx2 = m-1, n-1
        right = m+n-1
        while idx1 >= 0 or idx2 >=0:
            if idx1 == -1:
                nums1[right] = nums2[idx2]
                idx2 -= 1
            elif idx2 == -1:
                nums1[right] = nums1[idx1]
                idx1 -= 1
            elif nums2[idx2] > nums1[idx1]:
                nums1[right] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[right] = nums1[idx1]
                idx1 -= 1
            right -= 1