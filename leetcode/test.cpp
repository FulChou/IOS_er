#include <iostream>
#include <string>
#include <map>
#include <unordered_set>

using namespace std;

    bool isPalindromic(string s){
        int times = s.size()/2 + 1;
        int index1 = 0;
        int index2 = s.size()-1;
        
        while(times){
            times--;
            if(s[index1]!=s[index2]) return false;
            index1++;
            index2--;
        }
        return true;
    }
    string longestPalindrome(string s) {
        string result = "";
        int length = 0;
        for(int i=0;i<s.size();i++){
            for(int j=1;j<=s.size()-i;j+=2){
                string substr = s.substr(i,j);
                if(isPalindromic(substr)){
                    if(j>length){
                        cout<<"j:"<<j<<"sub:"<<substr<<endl;
                        length = j;
                        result = substr;
                    }
                }
            }
        }
        return result;
    }


int main(){
    string s = "cbbd";
    cout<<longestPalindrome(s);
    return 0;
}