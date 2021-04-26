# 2020.04.26: 二分搜索合适的 capacity：
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        '''
        思想就是去试：
        但是caipacity 从 0 开始 又太纯了，
        采用二分法去试就很好，low = max(weights), hight = sum(weights) 
        '''
        def is_within(mid,D):
            c = 0
            idx = 1
            for weight in weights:
                c += weight
                if c > mid:
                    c = weight
                    idx += 1
                    if idx > D:
                        return False
            return True
        low = max(weights)
        hight = sum(weights)
        while low < hight:
            mid = low + (hight - low) // 2
            if is_within(mid, D):
                hight = mid
            else: 
                low = mid + 1
        return hight
