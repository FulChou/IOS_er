#include<iostream>
#include<cstdio>
using namespace std;

int main(){
       int n,m;
    //scanf("%d %d",&n,&m);
    while(scanf("%d %d",&n,&m)!=EOF){
        if(n==0&&m==n) break;
         char table[n][m];
    // 输入数组 GT
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
           cin>>table[i][j];
        }
    int time;
    cin>>time;
    
    int col,raw;
    while (time)
    {   
        time--;
        scanf("%d %d",&raw,&col);
        if(col==0&&raw==0) break;
        // 给的要去计算匹配的数组：
        char table2[raw][col];
        for (int i = 0; i < raw; i++)
            for (int j = 0; j < col; j++)
            {
                cin>>table2[i][j];
            }
            // calculate
        int max = 0;
        for (int i = 0; i < n-raw+1; i++)
        {
            for (int j = 0; j < m-col+1; j++)
            {
                int sum=0;
                for (int k = 0; k < raw; k++)
                    for (int O = 0; O < col ; O++)
                    {
                        char x=table[i+k][j+O];
                        char y=table2[k][O];
                        // cout<<i<<j<<k<<O<<x<<" "<<y<<endl;
                       if(x==y) sum++;
                    }
                
                if(sum>max){
                    max=sum;
                }
            }
            
        }
        printf("%d\n",max);
    }

    }
    return 0 ;
}