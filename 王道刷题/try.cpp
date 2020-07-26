#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;

void PrintN(int N){
    int i;
    for( i=1;i<N;i++)
    printf("%d\n",i);
    return;
}

void PrintN1(int N){
    if(N){
        PrintN1(N-1);
        printf("%d\n",N);
        return;
    }
}

int main()
{
    bool temp = 1>(float)0/0;
    cout<< temp;
    
    return 0;
}
