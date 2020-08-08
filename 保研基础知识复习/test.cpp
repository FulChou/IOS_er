#include<iostream>
#include<string>
using namespace std;

union id{
    int id_num;
    char id_str;

} id_value;

int main(){
    id_value.id_num = 65;
    //id_value.id_str = 'A';
    cout<<id_value.id_str;
}