# 每日一题 2021.04.11
# 链接 ： https://leetcode-cn.com/problems/ugly-number-ii/
class Solution:
    import heapq
    def nthUglyNumber(self, n: int) -> int:
        # # 最小堆 解决方案：
        # factors = [2,3,5]
        # be_set = {1}
        # heap = [1]
        # idx = 1
        # heapq.heapify(heap)
        # while idx <= n:
        #     ugly = heapq.heappop(heap)
        #     for factor in factors:
        #         num = ugly * factor
        #         if num not in be_set:
        #             heapq.heappush(heap,num)
        #             be_set.add(num)
        #     idx += 1
        #     # size = len(be_set) #发现bug， 这样做只是输出了第n次算出来的数字， 第n个数字，并不是第n大的数.  应该是 第n次 pop 的数，肯定是第n大的数！！！
        # return ugly
        # 三个 坐标指针的方法，一次递增：
        res = [1]
        u_min = res[-1]
        idx = 0
        p2, p3, p5 = 0, 0, 0
        while idx < n-1:
            u2, u3, u5 = 2 * res[p2], 3 * res[p3], 5 * res[p5]
            u_min = min(u2,u3,u5)
            res.append(u_min)
            idx += 1
            if u_min == u2:
                p2 += 1
            if u_min == u3:
                p3 += 1
            if u_min == u5:
                p5 += 1
        return u_min

