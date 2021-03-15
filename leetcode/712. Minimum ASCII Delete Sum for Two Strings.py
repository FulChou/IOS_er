'''
Author: Ful Chou
Date: 2021-02-12 21:23:08
LastEditors: Ful Chou
LastEditTime: 2021-02-12 21:23:52
FilePath: /leetcode/712. Minimum ASCII Delete Sum for Two Strings.py
Description: What this document does
链接： https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/
'''
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        最小 删除和：
        dp：自顶向下：
        定义：dp(s1, idx1, s2, idx2) 是 s1 在 idx1 到 len(s1), s2 在 s2 在 idx2 到 len(s2) 时候的最小删除和
        既然可以自顶向下，那么就可以自底向上：
        明天来：
        '''
        ### 自顶向下：
        # memo = {}
        # def dp(s1, idx1, s2, idx2):
        #     if (idx1, idx2) in memo.keys():
        #         return memo[(idx1, idx2)]
        #     if idx1 == len(s1):
        #         res = 0
        #         while idx2 < len(s2):
        #             res += ord(s2[idx2])
        #             idx2 += 1
        #         return res 
        #     if idx2 == len(s2):
        #         res = 0
        #         while idx1 < len(s1):
        #             res += ord(s1[idx1])
        #             idx1 += 1
        #         return res
        #     if s1[idx1] == s2[idx2]:
        #         memo[(idx1, idx2)] = dp(s1, idx1+1, s2, idx2+1)
        #         return memo[(idx1, idx2)]
        #     else:
        #         memo[(idx1, idx2)] =  min(
        #             dp(s1, idx1+1, s2, idx2) + ord(s1[idx1]),
        #             dp(s1, idx1, s2, idx2+1) + ord(s2[idx2])
        #         )
        #         return memo[(idx1, idx2)]
        # res = dp(s1,0,s2,0)
        # return res

        ### 自底向上： 比 自顶向下更快，内存占用更小
        l1 = len(s1)
        l2 = len(s2)
        dp = [ [0]*(l2+1) for _ in range(l1+1)] # 初始条件有问题：
        # 相当于 自顶向下的 while 过程：
        for i in range(l1):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for j in range(l2):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1])
                    )
        return dp[l1][l2]
        ### 优化空间复杂度版本： 优化不了 ！



