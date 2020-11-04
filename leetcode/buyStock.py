# 第一题：

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        """
        状态转移方程  dp?
        dp_table[i][k][1] = max(dp_table[i-1][k][1],dp_table[i-1][k-1][0]-prices[i])
        dp_table[i][k][0] = max(dp_table[i-1][k][0],dp_table[i-1][k][1]+prices[i])
        """
        n = len(prices)
        if n == 0: return 0
        # dp_table = [[0] * 2 for i in range(n)] #取消了一个数组
        for i in range(0,n):
            if i == 0:
                # dp_table[0][1] = -prices[i]
                # dp_table[0][0] = 0
                # 节约内存写法：
                dp_i_1 = -prices[i]
                dp_i_0 = 0
                
            else:
                temp = dp_i_1
                dp_i_1 = max(dp_i_1,0-prices[i])
                dp_i_0 = max(dp_i_0,temp+prices[i])
        # print(dp_table)
        return dp_i_0


## 第二题：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        动归方程：
        dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0] - price[i])
        dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1] + price[i])
        k 无穷： 
        dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k][0] - price[i])
        dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1] + price[i])
        不需要k：
        dp[i][1] = max(dp[i-1][1],dp[i-1][0] - price[i])
        dp[i][0] = max(dp[i-1][0],dp[i-1][1] + price[i])
        """
        n = len(prices)
        if n == 0: return 0
        for i in range(0,n):
            if i == 0:
                dp_i_1 = -prices[i]
                dp_i_0 = 0
            else:
                temp = dp_i_1
                dp_i_1 = max(dp_i_1,dp_i_0 - prices[i])
                dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])
        return dp_i_0

## 第二种：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans
