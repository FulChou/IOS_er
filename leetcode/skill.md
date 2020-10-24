# skill for leetcode:

### map的基础用法：

1. operator []：
    使用[ ] 来进行元素插入，
2. 通过key找value :
   value = map[key] 
   value = map.at(key);
3. 查看是否存在key y
    m.count(y) > 0;
4. find(key) 返回指针，如果不是 m.end()，就是找到了


### BFS的解题框架：

```java

// 计算从起点 start 到终点 target 的最近距离
int BFS(Node start, Node target) {
    Queue<Node> q; // 核心数据结构
    Set<Node> visited; // 避免走回头路

    q.offer(start); // 将起点加入队列
    visited.add(start);
    int step = 0; // 记录扩散的步数

    while (q not empty) {
        int sz = q.size();
        /* 将当前队列中的所有节点向四周扩散 */
        for (int i = 0; i < sz; i++) {
            Node cur = q.poll();
            /* 划重点：这里判断是否到达终点 */
            if (cur is target)
                return step;
            /* 将 cur 的相邻节点加入队列 */
            for (Node x : cur.adj())
                if (x not in visited) {
                    q.offer(x);
                    visited.add(x);
                }
        }
        /* 划重点：更新步数在这里 */
        step++;
    }
    return -1 // 遍历完 还是没找到
}
```