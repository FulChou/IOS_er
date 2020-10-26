'''
滑动窗口，维护一个left - right 的滑动窗口：
1. 首先right 不停的向右移动，直到满足 覆盖到全部的关键k（t需要的字符）
一旦满足之后，我们也就是找到了一个解
然后右移 left 去找下一个解。
通过 begin 和 length 去存储最佳的解
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, valid = 0, 0, 0 #左右 index， 每一个key符合的valid数
        need = {}
        k_in_window = {} # 现有的window中 以及包含的 k of t(str)
        begin = 0
        length = float('inf')
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1 
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                if c in k_in_window:
                    k_in_window[c] += 1
                else:
                    k_in_window[c] = 1 
                if k_in_window[c] == need[c]:
                    valid += 1
            while valid == len(need): # 找到了所有t中的元素
                if (right - left) < length: # 有一个更短的子串
                    begin = left
                    length = right - left
                c = s[left]
                left += 1
                if c in need:
                    if k_in_window[c] == need[c]:
                        valid -= 1
                    k_in_window[c] -= 1
        if length == float('inf'):
            return ""
        return s[begin:length+begin]

if __name__ == "__main__":
    need = {}
    need['a'] = 1
    need['a'] += 1
    # print(len(need))
    string = "ADOBECODEBANC"
    print(string[9:4+9])