# 2021.04.27  最大分割子集：
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]: 
        # """
        # :type nums: List[int]
        # :rtype: List[int]
        # """
        # if not nums: return nums
        # if len(nums) == 1: return nums
        # l = len(nums)
        # nums.sort()

        # dp = [[i] for i in nums]
        
        # for i in range(1, l):
        #     for j in range(i-1, -1, -1):
        #         if nums[i]%nums[j] == 0:
        #             dp[i] = max(dp[j] + [nums[i]], dp[i],key=len)

        # return max(dp,key=len)
        n = len(nums)
        nums.sort()
        if n <= 1: return nums
        dp = [0] * n
        pre = [0] * n
        for i in range(n):
            lenth = 1
            pre_idx = -1
            for j in range(i):
                if nums[i] % nums[j] == 0: # 能整除
                    if  dp[j] + 1 > lenth:
                        lenth = dp[j] + 1
                        pre_idx = j
            dp[i] = lenth
            pre[i] = pre_idx
        # 到此为止，已经计算 最大分割子集数和其内容了，现在要通过回溯找出来
        max_len = 0
        max_idx = 0
        for i in range(n):
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        res = []
        i = 0
        while i < max_len:
            res.append(nums[max_idx])
            max_idx = pre[max_idx]
            i += 1
        res.reverse()
        return res
