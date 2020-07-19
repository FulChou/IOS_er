#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

bool isFour(int a,int b,int c,int d){
    int temp[4] = {a,b,c,d};
    sort(temp,temp+4);
    if((temp[0]+temp[1]+temp[2])>temp[3]){
        //cout<<temp[0]<<" "<<temp[1]<<" "<<temp[2]<<" "<<temp[3]<<endl;
        return true;
    }
    
    else return false;
}

int main(){
    int N;
    int a,b,c,d;
    vector<int> A,B,C,D;
    scanf("%d",&N);
   
    while (N>0)
    {   
        int count = 0;
        N--;
        // input
        for(int i=0;i<8;i++){
        int temp;
        cin>>temp;
        //cout<<temp;
        if(i<2){
            A.push_back(temp);
        }else if(i<4){
            B.push_back(temp);
        }else if(i<6){
            C.push_back(temp);
        }else
        {
            D.push_back(temp);
        } 
    }
    // 四层循环：
    for(int i=A[0];i<=A[1];i++){
        for(int j=B[0];j<=B[1];j++){
            for(int k=C[0];k<=C[1];k++){
                for(int o=D[0];o<=D[1];o++){
                if(isFour(i,j,k,o)){
                    count++;
                    }
                 }
            }
        }
    }

       // output:
       printf("%d\n",count);
    }
    return 0 ;
}