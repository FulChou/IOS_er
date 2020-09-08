#include<iostream>
#include<vector>

using namespace std;

struct Point
{
    int x;
    int y;
    char type;
    int tag;
};
struct Line
{
    int a0;
    int a1;
    int a2;
};

bool isline(vector<Point> A ,vector<Point> B,Line line){

    for(int i=0;i<A.size();i++){
        if(line.a0 + A[i].x * line.a1+ A[i].y*line.a2 > 0) 
             A[i].tag = 1;
             else  A[i].tag = 0;
    }
   for(int i=0;i<B.size();i++){
        if(line.a0 + B[i].x * line.a1+ B[i].y*line.a2 > 0) 
             B[i].tag = 1;
             else  B[i].tag = 0;
    }
    // a点不在同侧
    for(int i=1;i<A.size();i++){
        if(A[i].tag!=A[i-1].tag){
            //cout<<"a点不在同侧"<<endl;
            return false;
        }
       
    }
    // B 点不在同侧
    for(int i=1;i<B.size();i++){
        if(B[i].tag!=B[i-1].tag){
            //cout<<"B点不在同侧"<<endl;
            return false;
        }
        
    }
    // a,b 点在同侧
    if(A[0].tag==B[0].tag) return false;
    
    return true;
}

int main(){
    int n,m;
    cin>>n>>m;
    vector<Point> A,B;
    // input
    for(int i=0;i<n;i++){
        Point tempPoint;
        cin>>tempPoint.x;
        cin>>tempPoint.y;
        cin>>tempPoint.type;
        if (tempPoint.type=='A')    
        {
           A.push_back(tempPoint);
        }
           if (tempPoint.type=='B')    
        {
           B.push_back(tempPoint);
        }
    }

    for (int i = 0; i < m; i++)
    {
        Line line;
        cin>>line.a0;
        cin>>line.a1;
        cin>>line.a2;
        if(isline(A,B,line)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }

    return 0;
}