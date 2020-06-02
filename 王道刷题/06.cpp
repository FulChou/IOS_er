#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int h;
    while (scanf("%d",&h)!=EOF)
    {
        int row = h;
        int col = h+(h-1)*2;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(j<col-(h+i*2)){
                    printf(" ");
                }else{
                    printf("*");
                }
            }
            printf("\n");
        }
    }
    return 0;
}