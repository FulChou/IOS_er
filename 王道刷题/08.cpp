#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;

char str[81];
int n,n1,n2;

// 穷举法，解方程：
void calculateN(){
    n2 = 3;
        for (int i = 0; i < n; i++)
        {
            if (n2==n) break;
            n1=0; // n1 position;
            for (int j = 0; j < n2; j++)
            {
                n1++; 
                if (n1*2+n2-2==n)
                {
                    return;
                }
                
            }
            n2++;
        }
}
 // string 的知识：

int main(){
    string temp;
    while(getline(cin,temp)){
        // cout<<temp;
        n = temp.size();
        calculateN(); // 计算出 n1、n2
        char str[n1][n2];//
       // cout<<n<<n1<<n2;

        // fill the matrix str
        for (int i = 0; i < n1; i++)
        {
            for (int j = 0; j < n2; j++)
            {  
                if (i!=n1-1)
                {
                    if(j==0){
                        str[i][j] = temp.at(0);
                        temp.erase(0,1); // 从0位置开始，包括这个位置的 n-1的字符
                    }
                    else if(j==n2-1){
                        str[i][j] = temp.at(temp.size()-1);
                        temp.erase(temp.size()-1,1); 
                    }else
                    {
                        str[i][j] = ' ';
                    }
                }else{
                    str[i][j] = temp.at(0);
                    temp.erase(0,1);
                }
                
            }
        }
        // output
        for(int i=0;i<n1;i++){
            for(int j=0;j<n2;j++)
                cout<<str[i][j];
            cout<<endl;
        }
    }
    return 0;
}