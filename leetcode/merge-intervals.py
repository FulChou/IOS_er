'''
Author: Ful Chou
Date: 2020-12-25 16:24:47
LastEditors: Ful Chou
LastEditTime: 2020-12-25 16:25:13
FilePath: /leetcode/merge-intervals.py
Description: What this document does
链接： https://leetcode-cn.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        先将区间进行 begin 小优先，end 大优先的排序
        考虑区间的三种情况：
        1. 包含 l2[0] >= l1[0] and l2[1] <= l1[1] # res  只需要记住当前l1
        2. 区间2 和 区间1 部分相交    l1[0] <= l2[0] <= l1[1] and l2[1] > l1 [1] # 扩充当前的l1
        3. 不相交 l2[0] > l1[1] # 存储当前的l1，更新下一个l1
        '''
        n = len(intervals)
        if n == 1:
            return intervals
        import functools
        def cmp(l1,l2):
            if l1[0] < l2[0]:
                return -1
            elif l1[0] == l2[0]:
                if l2[1] >= l2[1]:
                    return -1
                else: return 1
            else: return 1
        intervals = sorted(intervals,key=functools.cmp_to_key(cmp))
        res = []
        window = intervals[0]
        for i in range(1,n):
            if intervals[i][0] >= window[0] and intervals[i][1] <= window[1]:
                pass
            elif intervals[i][0] >= window[0] and intervals[i][0] <= window[1] and intervals[i][1] > window[1]:
                window[1] = intervals[i][1]
            elif intervals[i][0] > window[1]:
                res.append(window)
                window = intervals[i]
        res.append(window)
        return res