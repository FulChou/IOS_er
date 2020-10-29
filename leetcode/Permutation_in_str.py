
#  2020.10.28日
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right, valid = 0, 0, 0
        need = {}
        k_window = {}
        for c in s1:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        # print(need)
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                if c in k_window:
                    k_window[c] += 1
                else: k_window[c] = 1
                if k_window[c] == need[c]:
                    valid += 1
            while (right - left) >= len(s1):
                if valid == len(need):
                    return True
                else:
                    c = s2[left]
                    left += 1
                    if c in k_window:
                        if k_window[c] == need[c]:
                            valid -= 1
                        k_window[c] -= 1
        return False