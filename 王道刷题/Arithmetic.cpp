#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

// data struct
struct CodeElement
{
    string name;
    double p;
    double left;
    double right;
};
// sort by youself;
CodeElement codeElememt [4] = {"A",0.1,0,0.1,"B",0.4,0.1,0.5,"C",0.2,0.5,0.7,"D",0.3,0.7,1.0};

double coderesult = 0.5143876;


string code = "CADACDB";
// 算数编码：还是不难的，如果提前把区间写出来，当然也可以自己算区间咯
int main(){
    double currentL = 0;
    double currentR = 1;
    double d ;
    int times = code.size();
    // 固定十六位：
    // cout<<fixed;
    cout.precision(10); // setting output precision
    for (int i = 0; i < times; i++)
    {
        //
        for (int j = 0; j < 4; j++)
        {   
            if(codeElememt[j].name.compare(code.substr(i,1))==0){
                double d = currentR-currentL;
                // 先算右边界：
                currentR = currentL+ codeElememt[j].right*d;
                // 左边界    
                currentL += codeElememt[j].left*d;
                // 输出
                cout<<currentL<<" " <<currentR<<endl;
            }
        }
    }
    // cout<<(0.5143876==0.5143876);
    // 译码：因为浮点数精度问题，不好比较；
    cout<<"--------------";
    double CL = 0;
    double CR = 1;
    string codeStr;
    while(CL!=coderesult){
        for (int i = 0; i < 4; i++)     
        {   
            double d = CR-CL;
            double TCR = CL+d*codeElememt[i].right;
            double TCL = CL+d*codeElememt[i].left;
            // if(coderesult==TCL){
            //     codeStr.append(codeElememt[i].name);
            //     break;
            // }
            if(coderesult<TCR&&coderesult>=TCL){
                codeStr.append(codeElememt[i].name);
                CR=TCR;
                CL=TCL;
                cout<<CL<<" "<<CR<<endl;
                //if(CR==coderesult) cout<<"hhhhhhh";
            }
            
        }
    }
    cout<<codeStr;
    return 0;
}