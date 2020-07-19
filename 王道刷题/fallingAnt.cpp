
//因为左右侧相同数目的蚂蚁互相抵消，他们的碰撞使得A的速度最终为0，
//而打破僵局的那个蚂蚁，就是第一个左右侧数目不对等的蚂蚁。
//（左3右4那就是右面第四个，左3右1那就是左面第二个）
//[referance](https://blog.csdn.net/csyifanZhang/article/details/105726123);

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;
struct Ant{
    int pos,v;
};
int MAX = 100;

bool cmp(Ant a,Ant b){
    return a.pos<b.pos;
}

int main(){
    Ant ants[MAX];
    vector<Ant> antL,antR;
    int n,s;
    cin>>n;
    //while ()
    //{
        for(int i=0;i<n;i++){
            cin>>ants[i].pos;
            cin>>ants[i].v;
            if(ants[i].v==0) s=i;//record 0 ant
        }
    
    for(int i=0;i<n;i++){
        if(ants[i].pos<ants[s].pos&&ants[i].v>0) antL.push_back(ants[i]);
        else if(ants[i].pos>ants[s].pos&&ants[i].v<0) antR.push_back(ants[i]);
    }
    // sort by pos
    sort(antL.begin(),antL.end(),cmp); sort(antR.begin(),antR.end(),cmp);
    int l = antL.size(); int r = antR.size();
    if(l==r){
        cout<<"Cannot fall!"<<endl;
    }else if(l>r){
         cout<<100-antL[l-r-1].pos<<endl;
    }else{
        cout<<antR[l].pos<<endl;// or antR[l].pos
    }
    return 0;
}