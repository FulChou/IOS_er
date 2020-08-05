# 排序：

### 简单排序：
- 基于比较的排序：
- 只讨论内部排序（全部数据放到内存）
- 稳定性：任意两个相等数据，排序前后的相对位置不发生改变

- 冒泡排序：稳定
  - 从上到下，最大的泡泡已经到了最后
  - ![](https://gitee.com/csu_vincent/images/raw/master/null/20200805134525.png)

- 插入排序： 打牌（插入排序）
  - ![](https://gitee.com/csu_vincent/images/raw/master/null/20200805140143.png)
  - 逆序对：对于下标i<j,如果a[i]>a[j],则称（i,j)是一对逆序对。
  - T(N,I)=O(N+I)// 交换2个相邻元素正好消去一个逆序对。
  - 如果序列基本有序，则插入排序简单且高效
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805142044.png)


```c++
void InsertionSort( ElementType A[], int N )
{ /* 插入排序 */
     int P, i;
     ElementType Tmp;
      
     for ( P=1; P<N; P++ ) {
         Tmp = A[P]; /* 取出未排序序列中的第一个元素*/
         for ( i=P; i>0 && A[i-1]>Tmp; i-- )
             A[i] = A[i-1]; /*依次与已排序序列中元素比较并右移*/
         A[i] = Tmp; /* 放进合适的位置 */
     }
}
```

### 希尔排序：Shell sort 不是稳定的
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805143034.png)

可以取不同的间隔，来提高希尔排序的效率，但是都不是很高

增量：D(k) = 2^k -1;

### 堆排序：

- 选择排序：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805160211.png)

- 堆排序：不稳定
  - 对于选择排序来说，找最小元素的过程，采用堆的方法来实现
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805160536.png)
- 算法二：采用最大堆，找到最大的元素然后与最后一个元素进行交换，然后堆的规模-1。
- ![](https://gitee.com/csu_vincent/images/raw/master/null/20200805161219.png)

```c++
void Swap( ElementType *a, ElementType *b )
{
     ElementType t = *a; *a = *b; *b = t;
}
  
void PercDown( ElementType A[], int p, int N )
{ /* 改编代码4.24的PercDown( MaxHeap H, int p )    */
  /* 将N个元素的数组中以A[p]为根的子堆调整为最大堆 */
    int Parent, Child;
    ElementType X;
 
    X = A[p]; /* 取出根结点存放的值 */
    for( Parent=p; (Parent*2+1)<N; Parent=Child ) {
        Child = Parent * 2 + 1;
        if( (Child!=N-1) && (A[Child]<A[Child+1]) )
            Child++;  /* Child指向左右子结点的较大者 */
        if( X >= A[Child] ) break; /* 找到了合适位置 */
        else  /* 下滤X */
            A[Parent] = A[Child];
    }
    A[Parent] = X;
}
 
void HeapSort( ElementType A[], int N ) 
{ /* 堆排序 */
     int i;
       
     for ( i=N/2-1; i>=0; i-- )/* 建立最大堆 */
         PercDown( A, i, N );
      
     for ( i=N-1; i>0; i-- ) {
         /* 删除最大堆顶 */
         Swap( &A[0], &A[i] ); /* 见代码7.1 */
         PercDown( A, 0, i );
     }
}
```

### 归并排序：稳定的 (nlogn)
merge操作：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805162547.png)

递归实现算法：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805164127.png)

非递归实现：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805165324.png)
![](https://gitee.com/csu_vincent/images/raw/master/null/20200805165254.png)

- 缺点需要一个额外的空间，很适合在“外排序”.

```c++
/* 归并排序 - 递归实现 */
 
/* L = 左边起始位置, R = 右边起始位置, RightEnd = 右边终点位置*/
void Merge( ElementType A[], ElementType TmpA[], int L, int R, int RightEnd )
{ /* 将有序的A[L]~A[R-1]和A[R]~A[RightEnd]归并成一个有序序列 */
     int LeftEnd, NumElements, Tmp;
     int i;
      
     LeftEnd = R - 1; /* 左边终点位置 */
     Tmp = L;         /* 有序序列的起始位置 */
     NumElements = RightEnd - L + 1;
      
     while( L <= LeftEnd && R <= RightEnd ) {
         if ( A[L] <= A[R] )
             TmpA[Tmp++] = A[L++]; /* 将左边元素复制到TmpA */
         else
             TmpA[Tmp++] = A[R++]; /* 将右边元素复制到TmpA */
     }
 
     while( L <= LeftEnd )
         TmpA[Tmp++] = A[L++]; /* 直接复制左边剩下的 */
     while( R <= RightEnd )
         TmpA[Tmp++] = A[R++]; /* 直接复制右边剩下的 */
          
     for( i = 0; i < NumElements; i++, RightEnd -- )
         A[RightEnd] = TmpA[RightEnd]; /* 将有序的TmpA[]复制回A[] */
}
 
void Msort( ElementType A[], ElementType TmpA[], int L, int RightEnd )
{ /* 核心递归排序函数 */ 
     int Center;
      
     if ( L < RightEnd ) {
          Center = (L+RightEnd) / 2;
          Msort( A, TmpA, L, Center );              /* 递归解决左边 */ 
          Msort( A, TmpA, Center+1, RightEnd );     /* 递归解决右边 */  
          Merge( A, TmpA, L, Center+1, RightEnd );  /* 合并两段有序序列 */ 
     }
}
 
void MergeSort( ElementType A[], int N )
{ /* 归并排序 */
     ElementType *TmpA;
     TmpA = (ElementType *)malloc(N*sizeof(ElementType));
      
     if ( TmpA != NULL ) {
          Msort( A, TmpA, 0, N-1 );
          free( TmpA );
     }
     else printf( "空间不足" );
}
//---------------------------------------------------------
/* 归并排序 - 循环实现 */
/* 这里Merge函数在递归版本中给出 */
 
/* length = 当前有序子列的长度*/
void Merge_pass( ElementType A[], ElementType TmpA[], int N, int length )
{ /* 两两归并相邻有序子列 */
     int i, j;
       
     for ( i=0; i <= N-2*length; i += 2*length )
         Merge( A, TmpA, i, i+length, i+2*length-1 );
     if ( i+length < N ) /* 归并最后2个子列*/
         Merge( A, TmpA, i, i+length, N-1);
     else /* 最后只剩1个子列*/
         for ( j = i; j < N; j++ ) TmpA[j] = A[j];
}
 
void Merge_Sort( ElementType A[], int N )
{ 
     int length; 
     ElementType *TmpA;
      
     length = 1; /* 初始化子序列长度*/
     TmpA = malloc( N * sizeof( ElementType ) );
     if ( TmpA != NULL ) {
          while( length < N ) {
              Merge_pass( A, TmpA, N, length );
              length *= 2;
              Merge_pass( TmpA, A, N, length );
              length *= 2;
          }
          free( TmpA );
     }
     else printf( "空间不足" );
```