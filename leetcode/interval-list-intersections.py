'''
Author: Ful Chou
Date: 2020-12-29 20:22:27
LastEditors: Ful Chou
LastEditTime: 2020-12-29 20:25:05
FilePath: /leetcode/interval-list-intersections.py
Description: What this document does
链接： https://leetcode-cn.com/problems/interval-list-intersections/

交替的去进行一个合并相交区间：
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = [] # 
        len_a = len(A)
        len_b = len(B)
        a_inx, b_inx = 0, 0
        while a_inx < len_a and b_inx < len_b:
            left = max(A[a_inx][0], B[b_inx][0])
            right = min(A[a_inx][1], B[b_inx][1])
            if left <= right:
                res.append([left, right])
            if A[a_inx][1] <= B[b_inx][1]:
                a_inx += 1
            else: b_inx += 1
        return res
