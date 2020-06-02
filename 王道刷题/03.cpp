#include <iostream>
#include <cstdio>

using namespace std;
// 得到相反的数
int getRevx(int x){
    int revx = 0;
    while(x!=0){
        revx *= 10;
        revx += x%10;
        x /= 10;
    }
    return revx;
}
//判断是否是对称
bool isSymmetry(int x){//
    if(x==getRevx(x))
        return true;
    return false;
}
int main (){
    for(int a=0;a<=256;a++){
        if(isSymmetry(a*a))
            printf("%d \n",a);
    }

    return 0;
}

// 第二章就完了，主要是学会了一些头文件、printf的使用。