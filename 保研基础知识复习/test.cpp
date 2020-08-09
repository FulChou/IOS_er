#include<iostream>
#include<fstream>
#include<string>
using namespace std;


union id{
    int id_num;
    char id_str;

} id_value;

int main(){
    ofstream outFile;
    outFile.open("text.md");
    outFile<<"# story of  lk love zf ";
    outFile.close();

    id_value.id_num = 65;
    //id_value.id_str = 'A';
    cout<<(1 and 1>2);
}