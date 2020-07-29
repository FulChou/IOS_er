#include<iostream>
#include<vector>
#include<string>
#include<map>

using namespace std;
// 还是不能用map呀； 因为map内部存储是无序的

struct Data{
  char name;
  vector<int> indexs;
};

int isHaveName(char x,vector<Data> datas){
    if(datas.size()>0){
        for(int i=0;i<datas.size();i++){
        if(x==datas[i].name) return i+1;// 找到同名的position；
        }
    }
    return 0;
}
int main(){
    string str;

    // map<char,vector<int> >datas;
    // map<char,vector<int> >::iterator iter;
    vector<Data> datas;
    while(cin>>str){

        datas.clear();
        for(int i=0;i<str.size();i++){
        int index= isHaveName(str[i],datas);
        //cout<<datas.size()<<endl;
        if(!index){
                vector<int> tempVector;
                tempVector.push_back(i);
                Data temp ;
                temp.name = str[i];
                temp.indexs = tempVector;
                datas.push_back(temp);
                //cout<<datas.size();
            }
        else{
                datas[index-1].indexs.push_back(i);
            }
        

        }

        for(int i=0;i<datas.size();i++){
            if(datas[i].indexs.size()>1){
                bool flag = false;
                for(int j=0;j<datas[i].indexs.size();j++){
                    if(flag)cout<<",";
                    flag=true;
                    cout<<datas[i].name<<":"<<datas[i].indexs[j];
                }
                cout<<endl;
            }
        }
        
    }
    return 0;
}