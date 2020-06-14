#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 // 别人19 模拟目录的做法；
int main()
{
    int n;
    vector<string> v, vs;
    vector< vector<string> > ve;
    while(cin>>n)
    {
        string str;
        if(n==0) return 0;
 
        v.clear();  //存放初始的所有行
        for(int i = 0; i<n; i++)
        {
            cin>>str;
            while(str[str.length()-1]!='\\') str+='\\';  //对每行进行处理，处理成最后有\字母的路径形式
            v.push_back(str);
        }
        sort(v.begin(), v.end());  //排序
 
        ve.clear();  //二维数组初始化
        for(int i = 0; i<v.size(); i++)
        {
            int begin = 0, end = 0;
            vs.clear();  //每个一维数组初始化
            while((end = v[i].find("\\", begin))!=string::npos){
                vs.push_back(v[i].substr(begin, end-begin));
                begin=end+1;
            }
            ve.push_back(vs);  //存放进二维数组中
        }
        for(int i = 0; i<n; i++)
        {
            if(i>0 && ve[i][0] == ve[i-1][0])  //与前一个目录有相同的根目录
            {
                int j = 1;
                while(j<ve[i].size() && ve[i][j]==ve[i-1][j]) j++;  //找到第一个不同的目录
                for(; j<ve[i].size(); j++)
                {
                    for(int k = 0; k<j; k++)
                        cout<<"  ";  //j是该目录在该路径中的下标，控制缩进的次数
                    cout<<ve[i][j]<<endl;
                }
            }
            else{
                for(int j = 0; j<ve[i].size(); j++)
                {
                    for(int k = 0; k<j; k++)
                        cout<<"  ";
                    cout<<ve[i][j]<<endl;
                }
            }
        }
        cout<<endl;  //每个测试用例最后都有一个空行
    }
    return 0;
}