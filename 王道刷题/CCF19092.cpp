#include <iostream>
#include <cstring>

using namespace std;

int N,op,k;
int flag[1010];
int num[1010];

int main(){
	memset(flag,0,sizeof(flag)); // 初始化
	memset(num,0,sizeof(num));
	cin>>N;
	for(int i = 0 ; i < N ; ++i){
		cin>>op;
		cin>>num[i];
		op--;
		while(op--){
			cin>>k;
			if(k > 0){
				if(num[i] > k){
					flag[i] = 1;
					num[i] = k;
				}
			}
			else{
				num[i] = num[i] + k;
			}
		}
	}

	long long T = 0;
	int D = 0,E = 0;
	// T D
	for(int i = 0 ; i < N ; ++i){
		T += num[i];
		if(flag[i] == 1){
			D++;
		}
	}
	// E:
	for(int i = 0 ; i < N ; ++i){
		if(flag[i]&&flag[(i+1)%N]&&flag[(i+2)%N]) // 循环
		E++;
	}
	cout<<T<<" "<<D<<" "<<E<<endl; 
	return 0;
}

/**

4
4 74 -7 -12 -5
5 73 -8 -6 59 -4
5 76 -5 -10 60 -2
5 80 -6 -15 59 0


5
4 10 0 9 0
4 10 -2 7 0
2 10 0
4 10 -3 5 0
4 10 -1 8 0

**/
