#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;

string str = "helloworld";
int main()
{
    // int n;
    // scanf("%d",&n);
    // getchar();
    // char temp[6][6];
    // for (int i = 0; i < n; i++)
    // {
    //     cin.getline(temp[i],n);
    // }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         cout<<temp[i][j];
    //     }
    //     cout<<endl;
        
    // }
    cout<<str.at(str.size()-1);
    str.erase(str.size()-1,1);
    cout<<str.at(str.size()-1);
    
    return 0;
}
