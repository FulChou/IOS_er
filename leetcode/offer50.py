'''
Author: Ful Chou
Date: 2020-12-22 14:24:47
LastEditors: Ful Chou
LastEditTime: 2020-12-22 17:02:26
FilePath: /leetcode/offer50.py
Description: What this document does
'''

# 链接：  https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

class Solution:
    def firstUniqChar(self, s: str) -> str:
        import collections
        dic = collections.defaultdict(int) # 默认值为0
        if len(s) == 0:
            return " "
        for c in s:
            dic[c] += 1
        res = ' '
        for key, value in dic.items():# 找得到的情况
            if value == 1:
                return key
        return res # 遍历完也找不到 key
    