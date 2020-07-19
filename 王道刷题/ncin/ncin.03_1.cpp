#include<stdio.h>
#define leap(x) (x%400==0||(x%4==0&&x%100!=0)?1:0)
#define Abs(x) ((x)>0?(x):-(x))
typedef struct date
{
    int y, m, d;
}Date;

const int yd[2][13]={{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
                     {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}};
                      
int days(Date x)
{
    int sum=0, i;
    int y=x.y, m=x.m, d=x.d;
    for(i=0; i<y; i++)
    {
        if(leap(i))
        {
            sum+=366;
        }
        else
        {
            sum+=365;
        }
    }
    for(i=1; i<m; i++)
    {
        sum+=yd[leap(y)][i];
    }
    sum+=d;
    return sum;
}
int main(void)
{
    Date a, b;
    int n;
    scanf("%d",&n);
    while(n>0) //读取固定的格式数据：
    {
        n--;
        scanf("%4d-%2d-%2d %4d-%2d-%2d", &a.y, &a.m, &a.d, &b.y, &b.m, &b.d);
        printf("%d\n", Abs(days(a)-days(b))+1);
    }
    return 0;
}