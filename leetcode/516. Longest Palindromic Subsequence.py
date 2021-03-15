'''
Author: Ful Chou
Date: 2021-02-13 22:42:15
LastEditors: Ful Chou
LastEditTime: 2021-02-13 22:43:08
FilePath: /leetcode/516. Longest Palindromic Subsequence.py
Description: What this document does
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence/
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = 1
        # for i in range(n-1,-1,-1):
        #     for j in range(i+1,n):
        #         if s[i] == s[j]:
        #             dp[i][j] = dp[i+1][j-1] + 2
        #         else:
        #             dp[i][j] = max(
        #                 dp[i+1][j],
        #                 dp[i][j-1]
        #             )
        # return dp[0][n-1]
        
        ## 使用一位数组，优化内存版本：
        dp = [1] * n
        for i in range(n-1,-1,-1):
            pre = 0
            for j in range(i+1,n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2 # 这里的 dp[i+1][j-1] 本轮 i 轮，需要i+1轮（上一轮）的[j-1]值， 需要自己去上一个 j（即[i+1],[j-1])被覆盖之前，将j-1 的值保存下来，留着下一轮使用
                else:
                    dp[j] = max(
                        dp[j],
                        dp[j-1]  # dp[j-1] = dp[i+1][j-1]
                    )
                pre = temp
        return dp[n-1]
