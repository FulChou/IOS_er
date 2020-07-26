#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct Student{
    int num;
    int grade;
};
vector<Student> students;

bool cmp(Student a,Student b){
    if(a.grade!=b.grade)
    return a.grade<b.grade;
    else return a.num<b.num;
}

int main(){
    int n;
    cin>>n;

    students.clear();
    for(int i=0;i<n;i++){
        Student student;
        cin>>student.num;
        cin>>student.grade;
        students.push_back(student);
    }
    sort(students.begin(),students.end(),cmp);
    // output
    for(int i=0;i<n;i++){
        cout<<students[i].num<<" "<<students[i].grade<<endl;
    }
    return 0;
}