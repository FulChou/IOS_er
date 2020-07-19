#include <iostream>
#include <vector>
#include<string>
#include <algorithm>

using namespace std;

int main(){
    int n;
    vector<string> inputLines;
    vector<string> v2;
    vector< vector<string> > v1; 
    while(cin>>n){
        if(n==0) break;
        string str;
        inputLines.clear(); // 每一次之前的 输入要清除掉。
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
        // 输出：
        for(int i = 0; i<n; i++)
        {
            if(i>0 && v1[i][0] == v1[i-1][0])  //与前一个目录有相同的根目录
            {
                int j = 1;
                while(j<v1[i].size() && v1[i][j]==v1[i-1][j]) j++;  //找到第一个不同的目录
                for(; j<v1[i].size(); j++)
                {
                    for(int k = 0; k<j; k++)
                        cout<<"  ";  //j是该目录在该路径中的下标，控制缩进的次数
                    cout<<v1[i][j]<<endl;
                }
            }
            else{
                for(int j = 0; j<v1[i].size(); j++)
                {
                    for(int k = 0; k<j; k++)
                        cout<<"  ";
                    cout<<v1[i][j]<<endl;
                }
            }
        }  
        
        // 破案了！！！ 就是可能前几个dir不同，但是后面的目录相同，
        // 所以我的这个方法，会导致输出不行，因为前面有不同的话，这就算是不同的目录了。 
        // 后面就不要再去判断 是否和前一个有相同目录了：
        // error：

        // for(int i=0;i<n;i++){
        //     for(int j=0;j<v1[i].size();j++){
        //         if(i > 0 &&v1[i][j]==v1[i-1][j]){// same character in the head
        //         }else{// new character
        //             for(int k = 0; k<j; k++)
        //                 cout<<"  ";
        //             cout<<v1[i][j]<<endl;
        //         }
        //     }
        // }

        cout<<endl;
    }
    return 0;
}