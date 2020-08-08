# 树：
表示层次关系：

插入、删除、查找：

引入：

查找：给定关键词k，从集合R中找到关键字与k相同的记录：
- 静态查找：集合里面是固定的
  - 方法一： 顺序查找 O(n);
  - 方法二：二分查找（binary Search）O(logn)
    - 条件：关键词有序存放，数组里面
    - 二分查找的次数，刚好是该节点所在的层数：
    - n个节点的判定树的深度：[log2n]+1
- 动态查找：集合里面记录是动态变化的

树的定义：
n（n>=0) 个节点构成的有限集合。
当n=0时，称为空树；

树有一个称为“根”的节点root，其余节点每个集合本身又是一个树，称为原来树的子树；

- 子树是不相交的：
- 除了根节点之外，每个节点有且仅有一个父节点；
- 一棵N个节点的树有N-1条边。

- 基本概念：

![](https://gitee.com/csu_vincent/images/raw/master/null/20200728144321.png)
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728144608.png)

- 树的实现方法：
  - 第一个儿子-兄弟表示法：

旋转就成了二叉树：

- 二叉树：
  - 由左子树和右子树两个不相交的二叉树组成；

斜二叉树：只有一边
完美二叉树：每层都满
完全二叉树：从左到右，从上到下来接子树

n0 = n2+1 :叶子节点数 = 度为2的节点数+1

![](https://gitee.com/csu_vincent/images/raw/master/null/20200728152337.png)
**遍历很重要：**

1. 顺序储存结构：
完全二叉树：按照从上至下、从左到右顺序存储n个节点的完全二叉树的节点父子关系：

父节点坐标：[i/2]
左儿子：2i 如果大于n，则表示没有这个左儿子
右儿子：2i+1

如果不是完全二叉树，就空间浪费去补齐。

2. 链表存储：

|left|data|right|

### 二叉树的遍历：对根来说的

1. 先序遍历：先根，后先序遍历其左右
2. 中序：     中序遍历左 根 中序遍历右
3. 后序：       后序遍历左 右 根
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728154030.png)

中序遍历非递归遍历算法：（使用堆栈）
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728154649.png)
4. 层次遍历：队列实现
   抛出一个，放入左右儿子；

由两种遍历确定二叉树：必须要有中序遍历才行：

例子：**先序和中序来确定一颗二叉树**：
使用中序，找到根节点，然后分开左子树，右子树。重复这个过程。

### 判断树是否同构：

结构数组表示二叉树：静态链表；

- 建树T1
- 建树T2
- 判断是否同构
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728165624.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200728170104.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200728170028.png)

### 二叉搜索树：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728170332.png)

找某一个元素，最小元素一定在树的最左边，最大元素一定在树的最右边；
- 查找
- 插入
递归的思想：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728171222.png)
- 删除：
  - 要删除的是叶节点：直接删除，父节点指针置为null
  - 要删除的节点只有一个子树：孩子节点代替父亲节点，指针代替：
  - 用另一个节点代替被删除节点：右子树最小元素或者左子树的最大元素。

递归思想真奥秘：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200728172650.png)

```c++
BinTree Insert( BinTree BST, ElementType X )
{
    if( !BST ){ /* 若原树为空，生成并返回一个结点的二叉搜索树 */
        BST = (BinTree)malloc(sizeof(struct TNode));
        BST->Data = X;
        BST->Left = BST->Right = NULL;
    }
    else { /* 开始找要插入元素的位置 */
        if( X < BST->Data )
            BST->Left = Insert( BST->Left, X );   /*递归插入左子树*/
        else  if( X > BST->Data )
            BST->Right = Insert( BST->Right, X ); /*递归插入右子树*/
        /* else X已经存在，什么都不做 */
    }
    return BST;
}
 
BinTree Delete( BinTree BST, ElementType X ) 
{ 
    Position Tmp; 
 
    if( !BST ) 
        printf("要删除的元素未找到"); 
    else {
        if( X < BST->Data ) 
            BST->Left = Delete( BST->Left, X );   /* 从左子树递归删除 */
        else if( X > BST->Data ) 
            BST->Right = Delete( BST->Right, X ); /* 从右子树递归删除 */
        else { /* BST就是要删除的结点 */
            /* 如果被删除结点有左右两个子结点 */ 
            if( BST->Left && BST->Right ) {
                /* 从右子树中找最小的元素填充删除结点 */
                Tmp = FindMin( BST->Right );
                BST->Data = Tmp->Data;
                /* 从右子树中删除最小元素 */
                BST->Right = Delete( BST->Right, BST->Data );
            }
            else { /* 被删除结点有一个或无子结点 */
                Tmp = BST; 
                if( !BST->Left )       /* 只有右孩子或无子结点 */
                    BST = BST->Right; 
                else                   /* 只有左孩子 */
                    BST = BST->Left;
                free( Tmp );
            }
        }
    }
    return BST;
}
```

### 平衡二叉树：

平衡因子：BF(T) = hL-hR
- 平衡二叉树(Valanced Binary Tree)(AVL树)
  - 空树，或者任意节点左右子树高度差不超过1，即｜BF（T）｜<1

- 给定节点数为n的AVL树的最大高度为 h = O(logn)

- 平衡二叉树的调整，保证还是个搜索树；

例题：是否是同一棵二叉搜索树：

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730151123.png)
3. 建造一个树，然后将另外的序列和现有的树进行比对，来判断是否一致。

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730152045.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730152407.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730152927.png)
- 去树中查找 序列中的数据： 要查找的过程中碰到没有找到过的元素，就不是同一个棵树了

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730153139.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730153359.png)
- 要一次把序列中全部的数读进来。。。可以加标记，读入全部的数，但是中间有已经失败的时候，就不去做判断了。

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730153902.png)

### 单链表逆转： 边界测试
![](https://gitee.com/csu_vincent/images/raw/master/null/20200730155005.png)

### 堆：
优先队列：特殊的“队列”，取出元素的顺序是依照元素的优先级，而不是元素进入队列的先后顺序。

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730160129.png)

特性：
- 完全二叉树
- 任意节点的关键字是子树所有节点的最大值（最小值）即 最大堆（最小堆）
![](https://gitee.com/csu_vincent/images/raw/master/null/20200730161827.png)

- 数组实现：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200730162152.png)

- 插入：完全二叉树来差，+ 换位置（跟父亲节点进行比较）i>1;或者index 等于0的时候，放一个很大的值。
![](https://gitee.com/csu_vincent/images/raw/master/null/20200730162537.png)

- 删除：O(logN)
![](https://gitee.com/csu_vincent/images/raw/master/null/20200730163240.png)

建立最大堆：将已经存在的N个元素按照最大堆的要求存放在一个一维数组中：
- 第二种方法更好：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200730163452.png)

- 建堆算法：O(n).从最后一个非叶子节点，开始比较，形成一个堆，从右边到左边再从下到上。

```c++
typedef struct HNode *Heap; /* 堆的类型定义 */
struct HNode {
    ElementType *Data; /* 存储元素的数组 */
    int Size;          /* 堆中当前元素个数 */
    int Capacity;      /* 堆的最大容量 */
};
typedef Heap MaxHeap; /* 最大堆 */
typedef Heap MinHeap; /* 最小堆 */
 
#define MAXDATA 1000  /* 该值应根据具体情况定义为大于堆中所有可能元素的值 */
 
MaxHeap CreateHeap( int MaxSize )
{ /* 创建容量为MaxSize的空的最大堆 */
 
    MaxHeap H = (MaxHeap)malloc(sizeof(struct HNode));
    H->Data = (ElementType *)malloc((MaxSize+1)*sizeof(ElementType));
    H->Size = 0;
    H->Capacity = MaxSize;
    H->Data[0] = MAXDATA; /* 定义"哨兵"为大于堆中所有可能元素的值*/
 
    return H;
}
 
bool IsFull( MaxHeap H )
{
    return (H->Size == H->Capacity);
}
 
bool Insert( MaxHeap H, ElementType X )
{ /* 将元素X插入最大堆H，其中H->Data[0]已经定义为哨兵 */
    int i;
  
    if ( IsFull(H) ) { 
        printf("最大堆已满");
        return false;
    }
    i = ++H->Size; /* i指向插入后堆中的最后一个元素的位置 */
    for ( ; H->Data[i/2] < X; i/=2 )
        H->Data[i] = H->Data[i/2]; /* 上滤X */
    H->Data[i] = X; /* 将X插入 */
    return true;
}
 
#define ERROR -1 /* 错误标识应根据具体情况定义为堆中不可能出现的元素值 */
 
bool IsEmpty( MaxHeap H )
{
    return (H->Size == 0);
}
 
ElementType DeleteMax( MaxHeap H )
{ /* 从最大堆H中取出键值为最大的元素，并删除一个结点 */
    int Parent, Child;
    ElementType MaxItem, X;
 
    if ( IsEmpty(H) ) {
        printf("最大堆已为空");
        return ERROR;
    }
 
    MaxItem = H->Data[1]; /* 取出根结点存放的最大值 */
    /* 用最大堆中最后一个元素从根结点开始向上过滤下层结点 */
    X = H->Data[H->Size--]; /* 注意当前堆的规模要减小 */
    for( Parent=1; Parent*2<=H->Size; Parent=Child ) {
        Child = Parent * 2;
        if( (Child!=H->Size) && (H->Data[Child]<H->Data[Child+1]) )
            Child++;  /* Child指向左右子结点的较大者 */
        if( X >= H->Data[Child] ) break; /* 找到了合适位置 */
        else  /* 下滤X */
            H->Data[Parent] = H->Data[Child];
    }
    H->Data[Parent] = X;
 
    return MaxItem;
} 
 
/*----------- 建造最大堆 -----------*/
void PercDown( MaxHeap H, int p )
{ /* 下滤：将H中以H->Data[p]为根的子堆调整为最大堆 */
    int Parent, Child;
    ElementType X;
 
    X = H->Data[p]; /* 取出根结点存放的值 */
    for( Parent=p; Parent*2<=H->Size; Parent=Child ) {
        Child = Parent * 2;
        if( (Child!=H->Size) && (H->Data[Child]<H->Data[Child+1]) )
            Child++;  /* Child指向左右子结点的较大者 */
        if( X >= H->Data[Child] ) break; /* 找到了合适位置 */
        else  /* 下滤X */
            H->Data[Parent] = H->Data[Child];
    }
    H->Data[Parent] = X;
}
 
void BuildHeap( MaxHeap H )
{ /* 调整H->Data[]中的元素，使满足最大堆的有序性  */
  /* 这里假设所有H->Size个元素已经存在H->Data[]中 */
 
    int i;
 
    /* 从最后一个结点的父节点开始，到根结点1 */
    for( i = H->Size/2; i>0; i-- )
        PercDown( H, i );
}
```




### 哈夫曼树与哈夫曼编码：

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730165358.png)

每次把权值最小的两颗二叉树合并：

- 使用最小堆（O(nlogn)
![](https://gitee.com/csu_vincent/images/raw/master/null/20200731161503.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200731161800.png)

- 哈夫曼编码： 代价最小

- 前缀码：任何字符的编码都不是另一个字符编码的前缀：
  - 可以无二义地解码

当编码都是二叉树的叶子节点时，可以保证编码是前缀码，解码无二义性；

### 集合及运算：

- 并查集：
每个节点都指向它的父亲（双亲表示法）

- 采用数组的存储方法：使用结构数组来表示就可以了，一个数据域，一个父亲的数组index，没有父亲则为-1；
  - 查找操作实现：从数组里面找x，没找到返回-1，找到后返回index-指到父亲节点的index。
  - 并运算：
    - 分别找到x1和x2两个元素所在集合树的根节点
    - 如果它们不同根，则将其中一个根节点的父节点指针设置成另一个根节点的数组下标。
    - 如果想要并的时候，不过多的增加树的高度，可以把小的集合合并到大的集合，（每个集合到底有多少个元素，可以采取，root节点存储的parent 指针为 -n，就是集合有n个节点）

```c++
#define MAXN 1000                  /* 集合最大元素个数 */
typedef int ElementType;           /* 默认元素可以用非负整数表示 */
typedef int SetName;               /* 默认用根结点的下标作为集合名称 */
typedef ElementType SetType[MAXN]; /* 假设集合元素下标从0开始 */
 
void Union( SetType S, SetName Root1, SetName Root2 )
{ /* 这里默认Root1和Root2是不同集合的根结点 */
    /* 保证小集合并入大集合 */
    if ( S[Root2] < S[Root1] ) { /* 如果集合2比较大 */
        S[Root2] += S[Root1];     /* 集合1并入集合2  */
        S[Root1] = Root2;
    }
    else {                         /* 如果集合1比较大 */
        S[Root1] += S[Root2];     /* 集合2并入集合1  */
        S[Root2] = Root1;
    }
}
 
SetName Find( SetType S, ElementType X )
{ /* 默认集合元素全部初始化为-1 */
    if ( S[X] < 0 ) /* 找到集合的根 */
        return X;
    else // 重要！！！！！
        return S[X] = Find( S, S[X] ); /* 路径压缩 */
}
```

### 例题：堆中的路径 
堆，完全二叉树，可以用数组实现；父亲就是i/2；

插入：
先找到位置，然后插入；
![](https://gitee.com/csu_vincent/images/raw/master/null/20200801154457.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200801154800.png)

### 例题：file transfer
简化集合，（对于数据类型是简单类型的集合来说，用序号表示数据，里面的内容放parent）

![](https://gitee.com/csu_vincent/images/raw/master/null/20200801170255.png)

![](https://gitee.com/csu_vincent/images/raw/master/null/20200801170435.png)

会超时间，是因为没有把小的树贴到大的树上，还可以进行（减少树的高度操作。）存

比树的高度：-树高
比集合的规模：-元素树  O（logN) 适合使用路径压缩。

路径压缩：反反复复的调用find，就会很快：