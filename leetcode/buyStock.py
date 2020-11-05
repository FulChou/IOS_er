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

### 第三题：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        状态转移方程  dp
        dp_table[i][k][1] = max(dp_table[i-1][k][1],dp_table[i-1][k-1][0]-prices[i])
        dp_table[i][k][0] = max(dp_table[i-1][k][0],dp_table[i-1][k][1]+prices[i])
        注意 base case 和 怎么处理k
                if i == 0:
                    dp_table[0][2][1] = -prices[i]
                    dp_table[0][2][0] = 0
                    dp_table[0][1][1] = -prices[i]
                    dp_table[0][1][0] = 0
                    # 规律 如果第一天 i=0的时候 买了 那么就是-prices[i]
                else:
                    dp_table[i][k][1] = max(dp_table[i-1][k][1], dp_table[i-1][k-1][0] - prices[i])
                    dp_table[i][k][0] = max(dp_table[i-1][k][0], dp_table[i-1][k][1] + prices[i])
        '''
        n = len(prices)
        #dp_table = [[[0 for t in range(2)]for i in range(3)] for j in range(n)] 初始化三维数组
        if n == 0: return 0
        for i in range(0,n):
            #for k in range(2,0,-1): 
            if i == 0:
                dp_i11 = -prices[i]
                dp_i10 = 0
                dp_i21 = -prices[i]
                dp_i20 = 0
                # 规律 如果第一天 i=0的时候 买了 那么就是-prices[i]
                # 如果不自己做一遍， 那么就是 直接有1 的为值 -无穷， i__0的值为0
            else:
                dp_i20 = max(dp_i20, dp_i21 + prices[i])
                dp_i21 = max(dp_i21, dp_i10 - prices[i])
                dp_i10 = max(dp_i10, dp_i11 + prices[i])
                dp_i11 = max(dp_i11, 0 - prices[i])
        
        return dp_i20