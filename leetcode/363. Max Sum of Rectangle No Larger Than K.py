# lc 363 ： 2021，04，22
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = -float('inf')
        for top in range(m): # top rim
            total_v = [0] * n
            for down in range(top,m): # down rim
                for j in range(n):
                    total_v[j] += matrix[down][j]
                sl = SortedList([0])
                s = 0
                for v in total_v:
                    s += v
                    bl = sl.bisect_left(s-k)
                    if bl < len(sl):
                        res = max(res,s-sl[bl])
                    sl.add(s)
        return res