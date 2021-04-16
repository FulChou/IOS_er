# 2021.04.16 hard: 
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        '''
        dp 问题：
        1. 子字符串应该一样长. 很简单已经保证了
          子字符串一样，那么久直接返回 True
        2. 子字符串中 存在的字母应该一样， 同一个字母的数量应该一样多 Count()
        两种分割方式，交换 或者 不交换不断的迭代下去：
        分割的两种方式要写对！
        '''
        @cache
        def dfs(idx1, idx2, length):
            if s1[idx1:length+idx1] == s2[idx2:idx2+length]:
                return True
            if Counter(s1[idx1:length+idx1]) != Counter(s2[idx2:idx2+length]):
                return False
            for i in range(1,length):
                # no swarp
                if dfs(idx1,idx2,i) and dfs(idx1+i, idx2+i, length-i): # 这两个的 位置 idx1, idx2 传入要注意:
                    return True
                if dfs(idx1, idx2+length-i, i) and dfs(idx1+i, idx2, length-i):
                    return True
            return False

        res = dfs(0,0,len(s1))
        dfs.cache_clear()
        # print(res)
        return res