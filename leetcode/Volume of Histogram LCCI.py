'''
Author: Ful Chou
Date: 2021-04-02 15:41:17
LastEditors: Ful Chou
LastEditTime: 2021-04-02 15:42:24
FilePath: /leetcode/Volume of Histogram LCCI.py
Description: What this document does
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        今天长见识了，学到了一个聪明的办法。
        水的体积 = 全部方块围起来的体积 - 方块体积
        '''
        height_sum = sum(height) # 方块体积
        all_heights = 0
        left, right = 0, len(height)
        level = 1
        while left < right:
            if height[left] >= level:
                if height[right - 1] >= level:
                    all_heights += (right - left)
                    level += 1
                else:
                    right -= 1
            else:
                left += 1
        return max(all_heights - height_sum,0)
