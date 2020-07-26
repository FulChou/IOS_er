# 2 线性结构：

## 2.1 线性表及其实现：
多项式的表示问题：

1. 方法一：顺序存储结构直接表示：

数组各分量对应多项式各项（有太多零项要表达，浪费

2. 方法二：顺序存储结构表示非零项：

使用结构数组来表示：

3. 方法三：链表结构存储非零项：

启示：
1. 同一个问题可以有不同的表示方法
2. 同一类共性问题：有序线性序列的组织和管理

**线性表**：由同类型数据元素构成有序序列的线性结构
- 表中的元素个数成为线性表的长度
- 线性表没有元素时，成为空表
- 表的起始位置成为表头，表结束位置成为表尾

![](https://gitee.com/csu_vincent/images/raw/master/null/20200725151940.png)




- 指针访问元素 ->
- 结构体访问元素 .
![](https://gitee.com/csu_vincent/images/raw/master/null/20200725152709.png)

- 顺序结果来实现：数组加一个last标识位；
1. 初始化
2. 求表长 last+1
3. find 时间效率O(n)
4. 插入，先移动后移动 O(n)
5. 删除，往前移动一位i--last元素O(n)

- 线性表链式存储实现：
1. 求表长：遍历一遍O(n)
2. 查找：遍历O(n)
3. 插入：插入一个链表 O(n)
4. 删除：n/2

- 广义表：

1. 广义表是线性表的推广
2. 对于线性表而言，n个元素都是基本的单元素
3. 广义表中，这些元素不仅可以是单元素也可以是另一个广义表

![](https://gitee.com/csu_vincent/images/raw/master/null/20200725160456.png)

- **多重链表**：

1. 多重链表中节点的指针域会有多个
2. 但是包含两个指针域的链表不一定是多重链表，比如在双向链表中，不是多重链表
3. 用途：存储树、图等复杂的数据结构

举例：矩阵可以用二维数组表示，但是对于稀疏矩阵，存储空间巨大浪费；

使用**十字链表**来进行存储
1. 只存储非0元素项：
   1. 节点的数据域：raw col value
2. 每个节点通过两个指针域，把同行、同列串起来：
   1. 行指针：right
   2. 列指针：Down


循环链表 ：是一种头尾相接的链表。其特点是无须增加存储量，仅对表的链接方式稍作改变，即可使得表处理更加方便灵活。

判断一个单向链表中是否存在环的最佳方法是 快慢指针 。

涉及遍历操作时，其终止条件变为判断它们是否等于某一指定指针，如头指针或尾指针等。

双向链表 :在单链表的每个结点里再增加一个指向其直接前趋的指针域prior。这样就形成的链表中有两个方向不同的链。双链表一般由头指针唯一确定的，将头结点和尾结点链接起来构成循环链表，并称之为双向链表。在有序双向链表中定位删除一个元素的平均时间复杂度为O(n),但是若指定节点，则可以直接删除当前指针所指向的节点。而不需要像单向链表中，删除一个元素必须找到其前驱。


## 2.2 堆栈：
具有操作约束的线性表：
只在一端进行操作，插入删除。（先入后出）LIFO

表达式求值，递归，函数调用，深度优先搜索，回溯算法；

对于n各元素的入栈问题，可能的出栈顺序有C(2n,n)/(n+1)个。（卡特兰数）


**后缀表达式求值策略**：从左到右扫描运算数和运算符 T(n)
1. 遇到运算数怎么办？ 入栈
2. 遇到运算符怎么办？ 从 堆栈中弹出适当数量运算数，计算并讲结果入栈
3. 最后，栈顶的元素就是表达式的结果值。

操作集：
1. CreateStack
2. IsFull
3. **Push**
4. IsEmpty
5. **Pop**:删除并返回栈顶元素

- 栈的顺序存储实现：
通常由一个一维数组和一个记录栈顶元素位置的变量组成：

- 栈的链式存储实现：单向列表来实现，top指针应该在链表头部，尾部找不到头节点

**中缀表达式求值** 中缀表达式转后缀表达式：
1. 运算数相对顺序不变
2. 运算符号顺序发生改变
   1. 需要储存“等待中”的运算符（堆栈）
   2. 要将当前符合与“等待中”的最后一个运算符号比较

![](https://gitee.com/csu_vincent/images/raw/master/null/20200725171908.png)

```c++
// 数组实现：
typedef int Position;
struct SNode {
    ElementType *Data; /* 存储元素的数组 */
    Position Top;      /* 栈顶指针 */
    int MaxSize;       /* 堆栈最大容量 */
};
typedef struct SNode *Stack;
 
Stack CreateStack( int MaxSize )
{
    Stack S = (Stack)malloc(sizeof(struct SNode));
    S->Data = (ElementType *)malloc(MaxSize * sizeof(ElementType));
    S->Top = -1;
    S->MaxSize = MaxSize;
    return S;
}
 
bool IsFull( Stack S )
{
    return (S->Top == S->MaxSize-1);
}
 
bool Push( Stack S, ElementType X )
{
    if ( IsFull(S) ) {
        printf("堆栈满");
        return false;
    }
    else {
        S->Data[++(S->Top)] = X;
        return true;
    }
}
 
bool IsEmpty( Stack S )
{
    return (S->Top == -1);
}
 
ElementType Pop( Stack S )
{
    if ( IsEmpty(S) ) {
        printf("堆栈空");
        return ERROR; /* ERROR是ElementType的特殊值，标志错误 */
    }
    else 
        return ( S->Data[(S->Top)--] );
}

// 链表实现：
typedef struct SNode *PtrToSNode;
struct SNode {
    ElementType Data;
    PtrToSNode Next;
};
typedef PtrToSNode Stack;
 
Stack CreateStack( ) 
{ /* 构建一个堆栈的头结点，返回该结点指针 */
    Stack S;
 
    S = (Stack)malloc(sizeof(struct SNode));
    S->Next = NULL;
    return S;
}
 
bool IsEmpty ( Stack S )
{ /* 判断堆栈S是否为空，若是返回true；否则返回false */
    return ( S->Next == NULL );
}
 
bool Push( Stack S, ElementType X )
{ /* 将元素X压入堆栈S */
    PtrToSNode TmpCell;
 
    TmpCell = (PtrToSNode)malloc(sizeof(struct SNode));
    TmpCell->Data = X;
    TmpCell->Next = S->Next;
    S->Next = TmpCell;
    return true;
}
 
ElementType Pop( Stack S )  
{ /* 删除并返回堆栈S的栈顶元素 */
    PtrToSNode FirstCell;
    ElementType TopElem;
 
    if( IsEmpty(S) ) {
        printf("堆栈空"); 
        return ERROR;
    }
    else {
        FirstCell = S->Next; 
        TopElem = FirstCell->Data;
        S->Next = FirstCell->Next;
        free(FirstCell);
        return TopElem;
    }
}
```

## 3.3 队列：
