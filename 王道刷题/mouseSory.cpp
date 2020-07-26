#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

struct Mouse
{
    int weight;
    string color;
};

bool cmp(Mouse a,Mouse b){
    return a.weight>b.weight;
}

int main(){
    int n;
    while (cin>>n)
    {
        Mouse mouses[n];
        for (int i = 0; i < n; i++)
        {
            cin>>mouses[i].weight;
            cin>>mouses[i].color;
        }
        sort(mouses,mouses+n,cmp);
        for (int i = 0; i < n; i++)
        {
            cout<<mouses[i].color<<endl;
        }
    }
    return 0;
}