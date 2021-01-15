'''
Author: Ful Chou
Date: 2021-01-15 19:02:55
LastEditors: Ful Chou
LastEditTime: 2021-01-15 19:03:30
FilePath: /leetcode/72.Edit-Distance.py
Description: What this document does
链接： https://leetcode-cn.com/problems/edit-distance/
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        动态规划，最重要的就是状态转移方程
        两种方式： 自顶向下， 自底向上：
        1. 自顶向下： 以及备忘录优化
        word1 -> idx1, word2 -> idx2
        base case:
        if idx1 == -1: return idx2 + 1
        if idx2 == -1: return idx1 + 1
        if word1[idx1] == word2[idx2]:
                return dp_top2base(idx1-1,idx2-1)
        min_val_in_idx1_idx2 = min(  # 存储在字典里面方便之后查找，节约时间复杂度，不能降低空间复杂度
                    dp_top2base(idx1, idx2 - 1) + 1, # add
                    dp_top2base(idx1 - 1, idx2) + 1, # delete
                    dp_top2base(idx1 - 1, idx2 - 1) + 1 # replace
                )

        2. 自底向上： 压缩状态空间 （经典
        if word1[i] == word2[j]:
                        table[i+1][j+1] = table[i][j]
                    else:
                        table[i+1][j+1] = min(
                            table[i][j+1]+1,
                            table[i+1][j]+1,
                            table[i][j]+1
                            )


        '''
        ### 自顶向下：空间占用 O(i*j) 实际上没有那么多###
        memo = {}
        def dp_top2base(idx1,idx2):
            if (idx1,idx2) in memo.keys():
                return memo[(idx1,idx2)]
            if idx1 == -1: return idx2 + 1
            if idx2 == -1: return idx1 + 1
            if word1[idx1] == word2[idx2]:
                return dp_top2base(idx1-1,idx2-1)
            else:
                memo[(idx1,idx2)] = min(# 存储在字典里面方便之后查找，节约时间复杂度，不能降低空间复杂度
                    dp_top2base(idx1, idx2 - 1) + 1, # add
                    dp_top2base(idx1 - 1, idx2) + 1, # delete
                    dp_top2base(idx1 - 1, idx2 - 1) + 1 # replace
                )
                return memo[(idx1,idx2)]

        ### 自底向上： 空间复杂度 O(i*j)  还可以继续优化： 到O( max(i,j) )###
        ## 优化策略： 一个一维数组 size max(i,j)

        # table = [[-1 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        # for i, table_raw in enumerate(table):
        #     table_raw[0] = i
        # for j in range(len(table[0])):
        #     table[0][j] = j
        # def dp_base2top(idx1,idx2):
        #     for i in range(idx1):
        #         for j in range(idx2):
        #             if word1[i] == word2[j]:
        #                 table[i+1][j+1] = table[i][j]
        #             else:
        #                 table[i+1][j+1] = min(
        #                     table[i][j+1]+1,
        #                     table[i+1][j]+1,
        #                     table[i][j]+1
        #                     )

        #     return table[idx1][idx2]
        n1 = len(word1) 
        n2 = len(word2)  
        # 有一个字符串为空串
        if n1 * n2 == 0:
            return n1 + n2
        return dp_top2base(n1-1,n2-1)