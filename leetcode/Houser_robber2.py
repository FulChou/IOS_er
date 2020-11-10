class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 : return 0
        if n == 1 : return nums[0]
        def dp(start,end):
            cur, pre = 0,0
            for i in range(start,end):
                pre, cur =  cur, max(cur, pre + nums[i])
            return cur
        return max(dp(0,n-1), dp(1,n)) # 拆分为两个线性问题