#include<iostream>
#include<cstdio>
#include<cstring>
const int maxN = 1000000;

using namespace std;

void getNext(char* p,int * next){
    next [0] = -1;
    int i=0;
    int j = -1;
    while(i<strlen(p)){
        if(j==-1||p[i]==p[j]){
            ++i;
            ++j;
            next[i]=j;
        }else j = next[j];
    }
}

int KMP(char* t,char* p,const int* next){
    int i=0,j=0;
    int num=0;
    while(i<strlen(t)){
        if(j==-1||t[i]==p[j]){
            ++i;
            ++j;
        }else j = next[j];
        if(j==strlen(p)){
            num++;
            j=next[j];
        }
    }
    return num;
    
}

int main(){
    //string T,P;
    char T[maxN+1];
    char P[maxN+1];
    
    while(scanf("%s %s",T,P)!=EOF){ // cin>> 会被换行符影响
        int next[strlen(P)]; // cstring 头文件中：
        getNext(P, next);
        cout<<KMP(T, P, next)<<endl;
    }
    
}