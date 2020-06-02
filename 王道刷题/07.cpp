#include<iostream>
#include<cstdio>
#include<math.h>
#include<string>

using namespace std;

    
    char templat [6][6]; //初始模版：
    char m2[3000][3000];// new template
    char result[3000][3000]; 
    int len; // new the size of matrix
    int n,q; // input n and q level

void update(int x,int y,bool flag) {
        // len 应该是此时（模版）的大小
        for (int i = 0;i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                if (flag)
                result [x+i][y+j] = m2[i][j]; // 每次更新一个模版大小的图形
                else 
                result [x+i][y+j] = ' ';
            }
            
        }
        
}

int main(){
    while(scanf("%d",&n)){
        // input and output is not in same buffer so，every time you can output the result array;
            if(0==n) break;
            //2.前面的scanf()在读取输入时会在缓冲区中留下一个字符'\n'（输入完s[i]的值后按回车键所致），
            //所以如果不在此加一个getchar()把这个回车符取走的话，gets(）就不会等待从键盘键入字符，
            //而是会直接取走这个“无用的”回车符，从而导致读取有误；
            getchar(); // take the \n
            for(int i=0;i<n;i++){
                //读入整行数据，它使用回车键输入的换行符来确定输入结尾。
                //调用方法: cin.getline(str (字符数组）, len);
            
            // 获取输入方法2:
            // string temp;
            // getline(cin,temp);
            // for (int j = 0; j < temp.size(); j++)
            //     templat[i][j] = temp[j];

            cin.getline(templat[i],6); // 获取输入方法1

            }
            
            scanf("%d",&q);
            for(int k=0;k<q;k++){
                len = pow(n,k);
                // first level：
                if(1==len){ // 边界条件 如果是k就是0，如果是len就是1
                    for (int i = 0; i < n; i++)
                        for(int j=0;j<n;j++){
                            m2[i][j] = templat[i][j];
                            result[i][j] = m2[i][j];
                        }
                }
                else{
                    // 1.分析模版，按照初始模版来替换 
                    for (int i = 0; i < n; i++)
                    {
                        for (int j = 0; j < n; j++)
                        {
                            if (templat[i][j]==' ')
                            update(i*len,j*len,false);
                            else 
                            update(i*len,j*len,true);
                        }
                        
                    }
                    // 3. 交换 此时的 模版和结果：
                    for (int i = 0; i < len*n; i++){
                    for (int j = 0; j < len*n; j++)
                        m2[i][j] = result[i][j];
                     }

                }
            }

        //输出
        len = pow(n,q);
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
                cout << result[i][j];
                 
            cout << endl;
        }

    }
    return 0;
}