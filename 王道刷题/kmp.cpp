#include <iostream>
#include <cstdio>

using namespace std;



void getNext(char * p, int * next)
{
	next[0] = -1;
	int i = 0, j = -1;

	while (i < strlen(p))
	{
		if (j == -1 || p[i] == p[j])
		{
			++i;
			++j;
			next[i] = j;
		}	
		else
			j = next[j];
	}
}

int KMP(char * t, char * p) 
{
	int i = 0; 
	int j = 0;

	while (i < strlen(t) && j < strlen(p))// 字符串没有匹配完，并且 这个模式没有匹配上
	{
		if (j == -1 || t[i] == p[j]) //
		{
			i++;
           	j++;
		}
	 	else 
           		j = next[j];
    }

    if (j == strlen(p))
       return i - j;
    else 
       return -1;
}


void printArr(int *next,int n){
    for (int i = 0; i < n; i++)
    {
        cout<<next[i]<<" ";
    }
    
}




int main(){

    int next[9];
    char str [10] = "abaabcabc";
    //{'a','b','a','a','b','c','a','b','c'};

    getNext(str,next);
    printArr(next,9);
    


    return 0 ;

    
}


