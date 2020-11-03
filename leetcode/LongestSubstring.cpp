
#include <iostream>
#include <string>
#include <map>
#include <unordered_set>

using namespace std;
// 维护一个滑动窗口：
int lengthOfLongestSubstring(string s) {
        // 感觉是在线处理： 不对 滑动窗口：
        int current,Maxl,i,j;
        int n=s.size();
        current=Maxl=i=j=0;
        unordered_set<char> unset;
        while(i<n &&j<n){
            
            if(!unset.count(s[j]) ){
                unset.insert(s[j]);
                j++;
                current = j-i;
                if(current>Maxl) Maxl = current;
            }else{
                unset.erase(s[i]);
                //current--;
                i++;
            }
        }
        return Maxl;
    }
/*  滑动窗口加 跳过充分的字符 i
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }
    */

/*
 # 代码时间意义不大，时间复杂度才是重点
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL, left, right = 0, 0, 0
        from collections import defaultdict
        window = defaultdict(int) # 可以用 set
        if len(s) == 1: return 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in window: # 如果已存在 c
                cL = s[left]
                print(cL,c)
                while cL != c:
                    del window[cL]
                    left += 1  
                    cL = s[left]
                left += 1 #找到已存在的那个c index 后一个字符
                length = right - left # 计算后一个字符 到c的lenth
                if length > maxL: # 记录最大长度
                    maxL = length
            else: 
                window[c] += 1 # 计算
                length = right - left # 计算后一个字符 到c的lenth
                if length > maxL: # 记录最大长度
                    maxL = length
        return maxL

# 方法二
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL, left, right = 0, 0, 0
        from collections import defaultdict
        window = defaultdict(int) # 还是用的dic
        if len(s) == 1: return 1
        while right < len(s): # 右移
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1: # 缩小window
                cL = s[left]
                left += 1
                window[cL] -= 1
            maxL = max(maxL,right-left)
        return maxL
*/