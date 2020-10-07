def fib(N):
        if N==0: return 0
        if N==1: return 1
        return fib(N-1) + fib(N-1)
def fib(self, N: int) -> int:
        if N <= 1:
            return N
        cache = {0: 0, 1: 1} # 自顶向下的话：要把这个tabel 初始化放到主函数里面：
        return self.memoize(cache,N)

def memoize(self,cache:{},N: int) -> int:
        for i in range(2,N+1): # 自低向上：
            cache[i] = cache[i-1] + cache[i-2]
        return cache[N]

if __name__ == "__main__":
    #sl = Solution()
    # print(fib(10))
    list1 = []
    list1.append(1)
    print(len(list1))