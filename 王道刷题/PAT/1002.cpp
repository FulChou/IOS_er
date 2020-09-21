#include<iostream>

using namespace std;


int K1,K2;

struct Point{
    int k;
    double a;
    Point* next;
    // construct function
    Point(){
        k=0;
        a=0;
        next = NULL;
    }
};

Point* read(int K,Point* p){
    Point* result = p, *temp;
    int x;
    double y;
     for (int i = 0; i < K; i++)
{
         temp = new Point;
         cin>>x>>y;
         temp->k = x;
         temp->a = y;
         temp->next = NULL;
         result->next = temp;
         result = temp;
         temp = NULL;

}
    //delete result;
    return p;
}

Point* add(Point* a,Point* b,Point* c){
    Point* result = c; // 局部变量，返回就没有了啊。。。
    Point* head = result;

    a = a->next;
    b = b->next;
    while (a && b)    
    {
        Point* p = new Point;
        if(a->k > b->k){
            p->a = a->a;
            p->k = a->k;
            a = a->next;
            result->next = p;
            result = result->next;
            
        }else if(a->k < b->k){
            p->a = b->a;
            p->k = b->k;
            result->next = p;
            b = b->next;
            result = result->next;
        }else{
            p->a = b->a + a->a;
            p->k = a->k;
            result->next = p;
            result = result->next;
            b = b->next;
            a = a->next;
        }
    }
    while (a)
    {
        result->next = a;
        result = a;
        a = a->next;
        
    }
    while (b)
    {
        result->next = b;
        result = b;
        b = b->next;
    }

    return head;
}
void printP(Point *p){
    
    int count=0;
    p = p->next;
    Point* result = p;
    while (p)
    {   
        if(p->a!=0) count++;
        p=p->next;
    }
    
    p = result; // replace pointer;

    if(count>0){ 
    cout<<count; // output count of point;
    while (p)
    {
        if(p->a!=0)
        printf(" %d %.1f",p->k,p->a);
        p = p->next;
        //cout<<" "<<p->k<<" "<<p->a;
    }

    }else 
    {
        cout<<0;
    }

}



int main(){
 
 Point *a=NULL,*b=NULL;
 //cout<<a<<" "<<b<<" "<<endl;
 
 cin>>K1;
 a = new Point;
//  a->a=0;
//  a->k=0;
//  a->next = NULL;
 a = read(K1,a);
 //cout<<"a:"<<a<<endl;
 cin>>K2;
 b = new Point;
//  b->a=0;
//  b->k=0;
//  b->next = NULL;
 b = read(K2,b);
//cout<<"b:"<<b<<endl;
//cout<<K2<<endl;
//  printP(a);
//  printP(b);
Point * result = new Point;
add(a,b,result);
// printP(a);
// printP(b);

printP(result);


    return 0;
}



/*

关联规则数据挖掘中最大频繁项集是什么
JAVA的内存管理和垃圾回收机制
B树和B+树的实现区别

kruskal prime dijstra floyd 快排 AVO LCA KMP 最简单的01背包  最长公共子序列 最长上升子序列 堆 dfs+树 无优化的bfs 贪心
平衡树 和 哈夫曼编码
2 1 2.4 0 3.2
2 2 1.5 1 0.5

*/