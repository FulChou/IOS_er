#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<ctime>
using namespace std;

void PrintN(int N){
    int i;
    for( i=1;i<N;i++)
    printf("%d\n",i);
    return;
}

void test(int N){
    for (int i = 0; i < N; i++)
    {
        // for (int j = 0; j < N; j++)
        // {
        //     cout<<i+j<<" ";
        // }
        // cout<<endl;
        cout<<i<<endl;
        
    }
    
}

int main()
{   
    clock_t start, end;
    start = clock();
    test(10);// 运行代码
    end = clock();
    cout<<"Run time: "<<(double)(end - start) / CLOCKS_PER_SEC<<"S"<<endl; // 头文件ctime

    return 0;
}
