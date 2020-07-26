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

    Country(){
        rank1 = 1;
        rank2 = 1;
        rank3 = 1;
        rank4 = 1;
    }
};

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
                // 比较 金牌数：
                if(needSort[i].goldNum<needSort[j].goldNum){
                     needSort[i].rank1++;
                }
                if(needSort[i].priceNum<needSort[j].priceNum){// 奖牌数
                    needSort[i].rank2++;
                }

                if(needSort[i].population<1&&needSort[i].goldNum!=0&&needSort[i].priceNum!=0){
                    
                }
                if(needSort[i].population<11&&needSort[i].goldNum==0){
                    
                    if((float)needSort[j].goldNum/needSort[j].population>0){
                        needSort[i].rank3++;
                        
                    } 
                }
                if(needSort[i].population<1&&needSort[i].priceNum==0){
                    
                    if((float)needSort[j].priceNum/needSort[j].population>0) needSort[i].rank4++;
                    
                }
                if(needSort[i].population>1){// 人数不为零的时候的 金牌，奖品人口比： 比值要记得换成float去进行比较！！！
                
                
                    if((float)needSort[i].goldNum/needSort[i].population<(float)needSort[j].goldNum/needSort[j].population){
                    needSort[i].rank3++;

                    
                    }
                        
                    if((float)needSort[i].priceNum/needSort[i].population<(float)needSort[j].priceNum/needSort[j].population){
                    needSort[i].rank4++;

                    // if(i==5) cout<<needSort[j].goldNum<<needSort[j].population;

                        }
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
        
        // output;
        // for (int i = 0; i < m; i++)
        // {
        //     cout<<needSort[i].rankResult<<":"<<needSort[i].sortType<<endl;
        // }
        cout<<needSort[5].rank1<<needSort[5].rank2<<needSort[5].rank3<<needSort[5].rank4<<endl;
        

    }
    return 0;
}