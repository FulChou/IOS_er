'''
Author: Ful Chou
Date: 2020-12-23 15:19:36
LastEditors: Ful Chou
LastEditTime: 2020-12-23 15:22:12
FilePath: /leetcode/offer10.py
Description: What this document does
'''
class Solution:
    """
    链接： https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
    2020.12.23 日 简单~
    """
    def numWays(self, n: int) -> int:
        '''
        1.
        画状态转移树 
        methods[i] = methods[i-1] + methods[i-2]
        2. 
        仔细思考只与前两个台阶有关：
        pre, cur = cur, (pre + cur)
        '''
        # # 解法1：
        # if n <= 1: return 1
        # methods = [-1 for i in range(n+1)]
        # methods[0] = 1
        # methods[1] = 1 
        # for i in range(2,n+1):
        #     methods[i] = methods[i-1] + methods[i-2]
        # return methods[n] % 1000000007
        # # 解法2：
        if n <= 1: return 1
        pre, cur = 1, 1
        for i in range(2,n+1):
            cur, pre = (pre + cur), cur
        return cur % 1000000007
    