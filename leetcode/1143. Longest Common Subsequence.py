'''
Author: Ful Chou
Date: 2021-01-22 17:12:42
LastEditors: Ful Chou
2021-01-22 17:14:25
LastEditTime: 2021-04-03 10:37:51
FilePath: /leetcode/1143. Longest Common Subsequence.py
Description: What this document does
https://leetcode-cn.com/problems/longest-common-subsequence/
第二次做： 21.04.03 清明节第一天
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        定义问题：
        dp函数的定义是：dp(s1, i, s2, j)计算s1[i..]和s2[j..]的最长公共子序列长度。
        先向 自顶向下的方法： 递归
        dp(s1, i, s2, j) = 
        if s1[i] == s2[j]:
            dp(s1, i-1, s2, j-1)
        else:  = max(
                    dp(s1, i+1, s2, j),
                    dp(s1, i, s2, j+1)
                )

        递推： 从第一个开始，推到最后一个元素：
        dp[i][j] ： 对于 i 位置的 text1， j位置的 text2 此时的最大公共子序列数：
        if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(
                        dp[i][j-1],
                        dp[i-1][j]
                        )
        这里的，二维状态压缩： 如何压缩呢？
        试图投影到一维数组：找到需要转移的值，以及临时存储的值
        '''
        ### 递归：
        # memo = {}
        # def dp(s1, i, s2, j):
        #     if i == len(s1) or j == len(s2): return 0
        #     if (i,j) in memo.keys():
        #         return memo[(i, j)]
        #     if s1[i] == s2[j]:
        #         memo[(i,j)] = 1 + dp(s1, i+1, s2, j+1)
        #         return memo[(i,j)]
        #     else:
        #         memo[(i,j)] = max(
        #             dp(s1, i+1, s2, j),
        #             dp(s1, i, s2, j+1)
        #         )
        #         return memo[(i,j)]
        # dp(text1,0,text2,0)
        # return memo[(0, 0)]
        # ### 递推：
        # n = len(text1)
        # m = len(text2)
        # dp = [ [0] * (m+1) for i in range(n+1)]
        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(
        #                 dp[i][j-1],
        #                 dp[i-1][j]
        #                 )
        # return dp[n][m]
        ### 递推：状态压缩： 删掉某一个维度，然后从 转换关系中 找到 需要的 邻接值：
        ##
        n = len(text1)
        m = len(text2)
        dp = [0] * (m+1)
        for i in range(1, n+1):
            pre = 0
            for j in range(1, m+1):
                temp = dp[j] # 拿到 下次的 i 需要的 dp[i-1][j-1]
                if text1[i-1] == text2[j-1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(
                        dp[j-1],
                        dp[j]
                        )
                pre = temp
        return dp[m]
