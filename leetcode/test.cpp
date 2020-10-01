#include <iostream>
#include <string>
#include <map>
#include <unordered_set>

using namespace std;

bool isunique(string s){
        map<char,int> dir;
        for(int i=0;i<s.size();i++){
            if(dir.count(s[i])) return false;
            else dir[s[i]] = 1;
        }
        return true;
    }

    int lengthOfLongestSubstring(string s) {
        // 感觉是在线处理： 不对
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
                cout<<i<<"s[i]: "<<s[i]<<endl;
                i++;
            }
        }
        return Maxl;
    }



int main(){
    string s = "pwwkew";
    int x =lengthOfLongestSubstring(s);
    cout<<x;
    return 0;
}