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





### 哈夫曼树与哈夫曼编码：

![](https://gitee.com/csu_vincent/images/raw/master/null/20200730165358.png)
