'''
Author: Ful Chou
Date: 2020-12-24 20:53:49
LastEditors: Ful Chou
LastEditTime: 2020-12-24 20:54:39
FilePath: /leetcode/remove-covered-intervals.py
Description: What this document does
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        import functools
        '''
        先排序 begin 从小到大，end 从大到小，然后再按照区间的相对位置进行三种不同的处理：
        1. 被包含
        2. 部分包含，右部分大于已有区间
        3. 区间完全不包含，直接更新现有区间
        图片说明
        '''
        n = len(intervals)
        if n == 1:
            return 1
        '''
        自定义排序:
        1. import functools
        2. 写好自定义的 排序函数cmp：要排序到前面的条件返回-1
        3. sorted(obj,key=functools.cmp_to_key(cmp))
        '''
        def sort_intervals(list1, list2):
            if list1[0] < list2[0]:
                return -1
            elif list1[0] == list2[0]:
                if list1[1] >= list2[1]:
                    return -1
                else: return 1
            else: return 1
        intervals = sorted(intervals, key=functools.cmp_to_key(sort_intervals))
        # print(intervals)
        windows = [0,0]
        cover_sum = 0
        for interval in intervals:
            if interval[0] >= windows[0] and  interval[1] <= windows[1]:
                cover_sum += 1
            elif interval[0] >= windows[0] and  interval[1] > windows[1]:
                windows[1] = interval[1]
            elif interval[0] > windows[1]:
                windows = interval
        return n - cover_sum