# 图： 多对多的关系
### 什么是图？
包含： 一组顶点：V（Vertex）表示顶点集合  一组边：E(Edge)边的集合

抽象数据类型定义：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200802193104.png)

带权重的树，叫网络。
- 表示：
  - 邻接矩阵[N][N]
    - 浪费一半的空间，可以采用N(N+1)/2的一维数组A存储，i行只有i个元素；  对应下标： （i*(i+1)/2+j)
    - 直观、简单，方便检查两点之间是否存在边
    - 方便计算任意顶点的度
    - 存稀疏图，十分浪费空间，统计边的时候（浪费时间）
  - 邻接表（适用于稀疏图）：G[N]为指针数组，对应矩阵每行一个链表，只存非0元素
    - 表示不唯一：
    - 方便找任意顶点点所有“邻接点”
    - 节约稀疏图的空间
    - 方便计算任意顶点的度：
      - 无向图：yes
      - 有向图：出度-容易，入度需要构造“逆邻接表”来计算
      - 检查任意两节点之间是否存在边：麻烦

### 图的遍历
1. DFS（Depth First Search）深度优先搜索：使用堆栈思想（递归）
![](https://gitee.com/csu_vincent/images/raw/master/null/20200802200025.png)
对于邻接表：$O(N+E)$
用邻接矩阵存储： $O(N^2)$

2. BFS（Breadth First Search）类似树的层序遍历：队列的思想
![](https://gitee.com/csu_vincent/images/raw/master/null/20200802200546.png)

为什么需要两种遍历？
面对不同的问题，两种遍历有不同的效果。

- 图不连通怎么办？：那就对多个顶点去做bfs或者dfs
![](https://gitee.com/csu_vincent/images/raw/master/null/20200802201512.png)
- 连通分量：
  - 极大顶点数：再加一个顶点就不连通了
  - 极大边树：包含子图中所有顶点相连点所有边

![](https://gitee.com/csu_vincent/images/raw/master/null/20200802201753.png)

```c++
/* 邻接表存储的图 - DFS */
 
void Visit( Vertex V )
{
    printf("正在访问顶点%d\n", V);
}
 
/* Visited[]为全局变量，已经初始化为false */
void DFS( LGraph Graph, Vertex V, void (*Visit)(Vertex) )
{   /* 以V为出发点对邻接表存储的图Graph进行DFS搜索 */
    PtrToAdjVNode W;
     
    Visit( V ); /* 访问第V个顶点 */
    Visited[V] = true; /* 标记V已访问 */
 
    for( W=Graph->G[V].FirstEdge; W; W=W->Next ) /* 对V的每个邻接点W->AdjV */
        if ( !Visited[W->AdjV] )    /* 若W->AdjV未被访问 */
            DFS( Graph, W->AdjV, Visit );    /* 则递归访问之 */
}

/* 邻接矩阵存储的图 - BFS */
 
/* IsEdge(Graph, V, W)检查<V, W>是否图Graph中的一条边，即W是否V的邻接点。  */
/* 此函数根据图的不同类型要做不同的实现，关键取决于对不存在的边的表示方法。*/
/* 例如对有权图, 如果不存在的边被初始化为INFINITY, 则函数实现如下:         */
bool IsEdge( MGraph Graph, Vertex V, Vertex W )
{
    return Graph->G[V][W]<INFINITY ? true : false;
}
 
/* Visited[]为全局变量，已经初始化为false */
void BFS ( MGraph Graph, Vertex S, void (*Visit)(Vertex) )
{   /* 以S为出发点对邻接矩阵存储的图Graph进行BFS搜索 */
    Queue Q;     
    Vertex V, W;
 
    Q = CreateQueue( MaxSize ); /* 创建空队列, MaxSize为外部定义的常数 */
    /* 访问顶点S：此处可根据具体访问需要改写 */
    Visit( S );
    Visited[S] = true; /* 标记S已访问 */
    AddQ(Q, S); /* S入队列 */
     
    while ( !IsEmpty(Q) ) {
        V = DeleteQ(Q);  /* 弹出V */
        for( W=0; W<Graph->Nv; W++ ) /* 对图中的每个顶点W */
            /* 若W是V的邻接点并且未访问过 */
            if ( !Visited[W] && IsEdge(Graph, V, W) ) {
                /* 访问顶点W */
                Visit( W );
                Visited[W] = true; /* 标记W已访问 */
                AddQ(Q, W); /* W入队列 */
            }
    } /* while结束*/
}
```
### 例题：拯救007 DFS算法：

### 例题：六度空间理论 广度优先算法 BFS算法：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200802210703.png)
保证六层的操作：
![](https://gitee.com/csu_vincent/images/raw/master/null/20200802210948.png)

### 最小生成树

### 最短路径