'''
Author: Ful Chou
Date: 2021-01-25 14:27:14
LastEditors: Ful Chou
LastEditTime: 2021-01-25 14:27:25
FilePath: /leetcode/583. Delete Operation for Two Strings.py
Description: What this document does
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        算出 最长公共子序列 res，然后用 
        n = len(word1)
        m = len(word2)
        return n - res + m - res
        '''
        n = len(word1)
        m = len(word2)
        dp = [0] * (m+1)
        for i in range(1, n+1):
            pre = 0
            for j in range(1, m+1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    '''
                    dp[j] : dp[i-1][j]
                    dp[i-1][j-1]: 等于啥呢？
                    '''
                    dp[j] = pre + 1
                else:
                    dp[j] = max(
                        dp[j-1],
                        dp[j]
                    )
                pre = temp
        lcs = dp[m]
        return m + n - 2 * lcs
