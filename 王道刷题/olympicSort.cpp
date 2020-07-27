#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

struct Country{
    int order;
    int goldNum;
    int priceNum;
    int population;
    int rank1;
    int rank2;
    int rank3;
    int rank4;
    int sortType;
    int rankResult;
    double valueForRank3();
    double valueForRank4();

   Country(){
        rank1 = 1;
        rank2 = 1;
        rank3 = 1;
        rank4 = 1;
    }
    // double valueForRank3(){
    //     if(population<1&&goldNum==0) return 0;
    //     if(population<1) return -1;
    //     else return (float) goldNum/population;
    // }
    // double valueForRank4(){
    //     if(population<1&&priceNum==0) return 0;
    //     if(population<1) return -1;
    //     else return (float) priceNum/population;
    // }

};
    double Country::valueForRank3(){
        if(population<1&&goldNum==0) return 0;
        if(population<1) return -1;
        else return (float) goldNum/population; // 要注意转成float！！！
    }
    double Country::valueForRank4(){
        if(population<1&&priceNum==0) return 0;
        if(population<1) return -1;
        else return (float) priceNum/population;
    }
    

int main(){
    int n,m;
    while (cin>>n>>m)
    {
        Country counties[n];
        for (int i = 0; i < n; i++)
        {   
            counties[i].order = i;
            cin>>counties[i].goldNum;
            cin>>counties[i].priceNum;
            cin>>counties[i].population;
        }

        Country needSort[m];

        for (int i = 0; i < m; i++)
        {
            int temp;
            cin>>temp;
            for (int j = 0; j < n; j++)
            {
                if(counties[j].order==temp)
                needSort[i] = counties[j];
            }
            
        }
        // sort:

        for (int i = 0; i < m; i++)
        {
            for(int j=0; j<m;j++){
                // 比较金牌数：
                if(needSort[i].goldNum<needSort[j].goldNum){
                     needSort[i].rank1++;
                }
                // 奖牌数
                if(needSort[i].priceNum<needSort[j].priceNum){
                    needSort[i].rank2++;
                }
                // 金牌比例：
                if(needSort[i].valueForRank3()==-1){
                    // if(needSort[j].valueForRank3()==-1) needSort[i].rank3++;
                }else
                {
                    if(needSort[j].valueForRank3()==-1) needSort[i].rank3++;
                    else if(needSort[i].valueForRank3()<needSort[j].valueForRank3()) needSort[i].rank3++;
                }
                // 奖牌比例：
                if(needSort[i].valueForRank4()==-1){
                    
                }else{
                    if(needSort[j].valueForRank4()==-1) needSort[i].rank4++;
                    else if(needSort[i].valueForRank4()<needSort[j].valueForRank4()) needSort[i].rank4++;

                }
                
            

            }
        }
        // 
        for (int i = 0; i < m; i++)
        {
                int min = m+1;
                
                if(needSort[i].rank1<min){
                    min = needSort[i].rank1;
                    needSort[i].sortType = 1;
                }
                if(needSort[i].rank2<min){
                    min = needSort[i].rank2;
                    needSort[i].sortType = 2;
                }
                if(needSort[i].rank3<min){
                    min = needSort[i].rank3;
                    needSort[i].sortType = 3;
                }
                if(needSort[i].rank4<min){
                    min = needSort[i].rank4;
                    needSort[i].sortType = 4;
                }
                needSort[i].rankResult = min;
        }
        
        //output;

        for (int i = 0; i < m; i++)
        {
            cout<<needSort[i].rankResult<<":"<<needSort[i].sortType<<endl;
        }
        //cout<<needSort[5].rank1<<needSort[5].rank2<<needSort[5].rank3<<needSort[5].rank4<<endl;
        

    }
    return 0;
}