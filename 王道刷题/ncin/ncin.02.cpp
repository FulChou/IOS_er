#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<string.h>


using namespace std;

bool myfunction (int i,int j) { return (i<j); }
bool myfunction1 (int i,int j) { return (i>j); }

int main(){
   
    int N;
    cin>>N;
    while (N>0)
    {   
        N--;
        if(N==0) break;
        vector<int> a;
        vector<int> b;
        int result=0;
        a.clear();
        b.clear();
        //input
        for (int i = 0; i < N; i++)
        {
            int temp;
            cin>>temp;
            a.push_back(temp);
        }
           for (int i = 0; i < N; i++)
        {
            int temp;
            cin>>temp;
            b.push_back(temp);
        }
        sort(a.begin(),a.end(),myfunction);
        sort(b.begin(),b.end(),myfunction1);
        for (int i = 0; i < N; i++)
        {
            result+=a[i]*b[i];
        }
        printf("%d\n",result);
        
    }
    return 0 ;
}