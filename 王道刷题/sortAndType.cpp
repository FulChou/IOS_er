#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

struct Student
{
    int order;
    int score;
    string name;
};
bool sortAscending(Student a,Student b){
    if(a.score==b.score) return a.order<b.order;
    else return a.score<b.score;
}
bool sortDescending(Student a,Student b){
    if(a.score==b.score) return a.order<b.order;
    else return a.score>b.score;
}
int main(){
    int n,type;
    while (cin>>n>>type)
    {
           
    Student students[n];

    for(int i=0;i<n;i++){
        students[i].order = i;
        cin>>students[i].name;
        cin>>students[i].score;
    }
    if (type==1)
    {
        sort(students,students+n,sortAscending);
    }else sort(students,students+n,sortDescending);

    for(int i=0;i<n;i++){
        cout<<students[i].name<<" "<<students[i].score<<endl;
    }

    }
    

    return 0;
}