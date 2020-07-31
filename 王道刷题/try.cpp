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
    string str1 = "abc";
    string str2 = "bc";
    if(str2>str1) cout<<string::npos;
    
    return 0;
}
