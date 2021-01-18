'''
Author: Ful Chou
Date: 2021-01-18 10:56:09
LastEditors: Ful Chou
LastEditTime: 2021-01-18 10:56:48
FilePath: /leetcode/1232 Check If It Is a Straight Line.py
Description: What this document does
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''
        1. 我的思路：
        ax1 + by1 + c = 0
        ax2 + by2 + c = 0
        a = y2 - y1
        b = x1 - x2
        c = -x1 * (y2-y1) - y1 * (x1 - x2)
        判断一个 新的点 x,y  是否符合 ax + by + c == 0 即可
        注意事项： 所以说打电话的时候做题，就会心思不集中，一直做错。
        
        2. 看题解思路： k 的求法， 除法移相 变成乘法：
        pre_k = y2 - y1 / x2 - x1 == cur_k = y3 - y2 / x3 - x2 
        变成 (x2 - x1)*(y3 - y2) == (x3 - x2) * (y2 - y1)
        即： pre_deta_x * cur_deta_y == cur_deta_x * pre_deta_y
        实现细节：看代码
        '''
        #### 方法一： #####
        # if len(coordinates) <= 2:
        #     return True
        # pre_a, pre_b = coordinates[1][1] - coordinates[0][1], coordinates[0][0] - coordinates[1][0]
        # pre_c = -coordinates[0][0] * pre_a - coordinates[0][1] * pre_b
        # for i in range(2, len(coordinates)):
        #     if pre_a * coordinates[i][0] + pre_b * coordinates[i][1] + pre_c != 0:
        #         return False
        # return True

        #### 方法二： ####
        if len(coordinates) <= 2:
            return True
        pre_deta_y = coordinates[1][1] - coordinates[0][1]
        pre_deta_x = coordinates[1][0] - coordinates[0][0]
        for i in range(2, len(coordinates)):
            cur_deta_y = coordinates[i][1] - coordinates[i-1][1]
            cur_deta_x = coordinates[i][0] - coordinates[i-1][0]
            if cur_deta_y * pre_deta_x != cur_deta_x * pre_deta_y:
                return False
        return True