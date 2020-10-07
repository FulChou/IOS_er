# coding=UTF-8
    #自低向上：
# def dp(dp_table,coins, amount) :
#     # print(dp_table[0])
#     for i in range(1,amount+1):
#         res = float('inf')
#         for coin in coins:
#             if i-coin < 0 : continue
#             res = min(res,dp_table[i-coin] +1) # 发现问题了，如果使用res 那么 第一个进来的0，就会变成-1 改变range 也可以修正答案
#             #dp_table[i] = min(dp_table[i],dp_table[i-coin] +1)
#             print("i:"+str(i)+"coin:"+str(coin)+"res:"+str(res)+"table[i-coin]:"+str(dp_table[i-coin])+"\n")
#         dp_table[i] = res  if res != float('inf') else -1
#     return dp_table[amount] if dp_table[amount] != float('inf') else -1

def coinChange(coins, amount):
    #dp_table = {0:0}
    dp_table = [float('inf')] * (amount+1)
    dp_table[0] = 0
    return dp(dp_table,coins,amount)


#自顶向下：
def dp(self,dp_table:[float],coins: List[int], amount: int) ->int:
        if amount == 0:return 0
        if amount < 0 :return -1
        if dp_table[amount] != float('inf'):
            return dp_table[amount]
        # 求最小值：
        res = float('inf')
        for coin in coins: # 每次选择的都是让 amount 减少最多的
            subpb = self.dp(dp_table,coins,amount-coin)
            if subpb == -1:
                continue
            res = min(res,subpb+1)
        dp_table[amount] = res if res != float('inf') else -1
        return dp_table[amount]

if __name__ == "__main__":
    lists = [1,2,5]
    amount = 11
    print('res:',coinChange(lists,amount))