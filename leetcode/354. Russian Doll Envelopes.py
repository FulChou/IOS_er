'''
Author: Ful Chou
Date: 2021-01-18 11:57:24
LastEditors: Ful Chou
LastEditTime: 2021-01-18 11:57:38
FilePath: /leetcode/354. Russian Doll Envelopes.py
Description: What this document does
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        先排序，然后考虑一个最长上升子序列问题：
        链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/pythonguan-fang-ti-jie-si-lu-liang-chong-zp4g/

        '''
        def Env_cmp(x,y):
            if x[0] < y[0]:
                return -1
            elif x[0] == y[0]:
                if x[1] >= y[1]:
                    return -1
                else: return 1
            else: return 1
        import functools
        envelopes.sort(key=functools.cmp_to_key(Env_cmp))
        print(envelopes)
        ### 排序完之后， 考虑一个最长上升子序列问题：
        dp = []
        for pair in envelopes:
            h = pair[1]
            if not dp or h > dp[-1]:
                dp.append(h)
            else:
                left, right = 0, len(dp)
                while left < right:
                    mid = (left + right) // 2
                    if h > dp[mid]:
                        left = mid + 1
                    elif h <= dp[mid]:
                        right = mid
                dp[left] = h
        return len(dp)