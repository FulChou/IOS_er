#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

const int MAXN = 110000;

vector<int> prime;
bool table[MAXN];

int initial(bool* table,int n){
    prime.clear();
    for(int i=0;i<n;i++){
        table[i] = true;
    }
    double bound = sqrt(n);
    table[0]=false;
    table[1]=false;
    for(long long i=2;i<n;i++){
        if(!table[i]) continue; // 不是质数
        prime.push_back(i);
        //int j = i*i;
        if(i>=bound) continue; // 如果i超过一般，i*i一定会超过n，没必要进行计算了。加了这一句，g++ 运行就没问题了。。。确实可以节约一些操作,找到原因了 
        //int 大概是 -2^31 ~ 2^31-1 对应十进制： 2 * 10^10次的大小，所以不能六位乘六位。int会溢出，然后访问到不对的内存。这就是为什么数据不能太大。
        // 换成long long 也是对的；
        for(long long j=i * i;j<n;j+=i){ // g++ 出错
        //cout<<j<<endl;
        if(j>0&&j<n) table[j] = false;
            // cout<<table[j];
        }
        
    }
    return prime.size();
}

int main(){
    
    int k;
    initial(table, MAXN); // 求出 2-MAX 的所有质数；
    //cout<<prime.size();
    while (cin>>k)
    {
        cout<<prime[k-1]<<endl;
    }
    
    
    return 0;
}

