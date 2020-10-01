
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