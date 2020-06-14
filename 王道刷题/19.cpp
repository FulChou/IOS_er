#include <iostream>
#include <vector>
#include<string>
#include <algorithm>

using namespace std;

int main(){
// clock_t start, finish;
//double totaltime;
//start = clock();



    int n;
    vector<string> inputLines;
    vector<string> v2;
    vector< vector<string> > v1; 
    while(cin>>n){
        if(n==0) break;
        string str;
        for(int i=0;i<n;i++){
            cin>>str;
            if(str[str.size()-1]!='\\') str+='\\';
            inputLines.push_back(str);
        }
        sort(inputLines.begin(),inputLines.end()); //每一行排序

        v1.clear();
        //vector<string> v2;  remove '//'    error: 这样区分不出单字母的目录和多字母的目录
        for(int i=0;i<inputLines.size();i++){
            int begin = 0;
            v2.clear();// clear v2;
            for(int j=0;j<inputLines[i].size();j++){
                if(inputLines[i][j]=='\\'){
                    v2.push_back(inputLines[i].substr(begin,j-begin));
                    begin=j+1;// skip '\\';
                }
            }
            // 放到v1中； 
            v1.push_back(v2);
        }
        // output;
        for(int i=0;i<v1.size();i++){
            for(int j=0;j<v1[i].size();j++){
                if(i!=0&&v1[i][j]==v1[i-1][j]){// same in the head
                    continue;
                }else{// new 
                    for(int k=0;k<j;k++){
                        cout<<"  ";
                    }
                    cout<<v1[i][j]<<endl;
                }
            }
        }
        cout<<endl;
    }
    //finish = clock();
    //totaltime = (double)(finish - start) / 1000000;
    //printf("\n此程序的运行时间为%f秒", totaltime);
    return 0;
}