#include<iostream>
#include<string.h>
#include<cstdio>

using namespace std;

int main(){
  string str;
  string substr;
//   char head [100] ;
//   char tail [100] ;
  
  cin>>str;
  substr = "";
  bool flag = true;
  for(int i=0;i<str.size();i++){
      char x1 = str[i];
      char x2 = str[str.size()-1-i];
      if(x1==x2){
          substr.append(str.substr(i,1));
      }
      if(x1!=x2) 
      cout<< substr;
      return 0;
  }
return 0;
}