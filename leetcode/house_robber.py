
### 198 house robber: 11.09 08:22

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        ### 这个是逆着 dp
        ### dp[i] = max(dp[i+1], dp[i+2] + nums[i]) 从 0到第i间 屋子偷窃的钱
        # max_table = [-1 for i in range(n)] # 记忆table
        # def dp(start:int, n:int):
        #     if start >= n:
        #         return 0
        #     elif max_table[start] != -1:
        #         return max_table[start]
        #     else:
        #         res = max(dp(start + 1, n), dp(start + 2, n) + nums[start])
        #         max_table[start] = res
        #         return res
        # return dp(0,n)

        ### 顺着的 dp：
        dp_i, dp_i1, dp_i2 = 0, 0, 0
        for i in range(n-1,-1,-1):
            dp_i = max(dp_i1 ,dp_i2 + nums[i])
            dp_i2 = dp_i1
            dp_i1 = dp_i
            # print(i,dp_i)
        return dp_i
