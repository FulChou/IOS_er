'''
Author: Ful Chou
Date: 2021-04-04 11:46:01
LastEditors: Ful Chou
LastEditTime: 2021-04-04 11:46:11
FilePath: /leetcode/781. Rabbits in Forest.py
Description: What this document does
'''
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import defaultdict
        rabbit_dit = defaultdict(int)
        for rabbit in answers:
            rabbit_dit[rabbit] += 1 
        sum_r = 0
        for k, v in rabbit_dit.items():
            if k == 0:
                sum_r += v
            elif v % (k+1) == 0:
                sum_r += v
            else:
                sum_r += (v//(k+1) + 1) * (k + 1)
            print(sum_r)
        return sum_r
        ## 官方答案： Counter可还行！
        count = Counter(answers)
        ans = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
        # x + y 是向上取整的另一种表达方式，比如 4/5向上取整可以改成 （4+5）/ 5，减少了函数的调用
        return ans