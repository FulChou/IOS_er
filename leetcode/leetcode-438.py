class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: # 继续默写 滑动窗口解题框架：
        left, right, valid = 0, 0, 0
        result = []
        # k_of_window = {}
        # need = {}
        from collections import defaultdict
        need=defaultdict(int)
        k_of_window=defaultdict(int) # 默认会构造，对于一个不存在的k，初始value为0
        for c in p:
            need[c] += 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                k_of_window[c] += 1
                if k_of_window[c] == need[c]:
                    valid += 1
            while (right - left) >= len(p):
                if valid == len(need):
                    result.append(left)
                c = s[left]
                left += 1
                if c in need:
                    if k_of_window[c] == need[c]:
                        valid -= 1
                    k_of_window[c] -= 1
        return result