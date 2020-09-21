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
 
 Point *a=NULL,*b=NULL;  // 声明指针的时候 初始化 address 或者给NULl
 //cout<<a<<" "<<b<<" "<<endl;
 
 cin>>K1;
 a = new Point;  //  创建一个指针块
 a = read(K1,a);
 //cout<<"a:"<<a<<endl;
 cin>>K2;
 b = new Point;

 b = read(K2,b);

Point * result = new Point;
add(a,b,result);
printP(result);
    return 0;
}
/*

2 2 1.5 1 0.5

*/