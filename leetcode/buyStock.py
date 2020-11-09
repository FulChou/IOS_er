### 股票题，三维 DP
# 第一题： 11.03晚上做完

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
                dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        return dp_i_0

    ### 第二种方法：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans

### 第三题： k = 2
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

### 第四题 任意k次交易：
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        if k > n / 2:
            dp_ik0 = 0
            dp_ik1 = -float('inf')
            for i in range(0,n):
                temp = dp_ik0
                dp_ik0 = max(dp_ik0, dp_ik1 + prices[i])
                dp_ik1 = max(dp_ik1, temp - prices[i])
            return dp_ik0
        else:
            # dp_table = [[[0 for d in range(2)] for k in range(k + 1)]for i in range(n)]
            # 优化不需要存储 时间i 维度。 当前时刻的最优解只与 前一个时刻有关
            dp_table = [[0 for d in range(2)] for k in range(k + 1)]
            maxk = k 
            for i in range(0,n):
                for k in range(maxk,0,-1): # 注意这个 -1 不然里面的循环都不会进行了, 注意 k in range（k） 下一次k会混乱
                    if i == 0:
                        dp_table[k][0] = 0
                        dp_table[k][1] = -prices[i]
                    else:
                        dp_table[k][0] = max(dp_table[k][0], dp_table[k][1] + prices[i])
                        dp_table[k][1] = max(dp_table[k][1], dp_table[k-1][0] - prices[i])
            # print(dp_table)
            # print(k)
            return dp_table[maxk][0]

### 第五题 带[冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp_table = [[0 for n in range(2)] for i in range(n)]
        for i in range(0,n):
            if i == 0:
                dp_table[0][0] = 0
                dp_table[0][1] = -prices[i]
            elif i == 1:
                dp_table[1][0] = max(dp_table[0][0], dp_table[0][1] + prices[i])
                dp_table[1][1] = max(dp_table[0][1], -prices[i]) 
            else:
                dp_table[i][1] = max(dp_table[i-1][1], dp_table[i-2][0] - prices[i])
                dp_table[i][0] = max(dp_table[i-1][0], dp_table[i-1][1] + prices[i])
        # print(dp_table)
        return dp_table[n-1][0]

### 第六题 手续费： [链接](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
### 11.09号
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0: return 0
        for i in range(0, n):
            if i == 0:
                dpi0 = 0
                dpi1 = -prices[i]
            else:
                temp = dpi1
                dpi1 = max(dpi1, dpi0 - prices[i])
                dpi0 = max(dpi0, temp + prices[i] - fee)
        return dpi0
