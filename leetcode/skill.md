# skill for leetcode:

##  刷题的总结:

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

### 二分查找解题框架：

``` java
int binary_search(int[] nums, int target) {
    int left = 0, right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1; 
        } else if(nums[mid] == target) {
            // 直接返回
            return mid;
        }
    }
    // 直接返回
    return -1;
}

int left_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定左侧边界
            right = mid - 1;
        }
    }
    // 最后要检查 left 越界的情况
    if (left >= nums.length || nums[left] != target)
        return -1;
    return left;
}


int right_bound(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] == target) {
            // 别返回，锁定右侧边界
            left = mid + 1;
        }
    }
    // 最后要检查 right 越界的情况
    if (right < 0 || nums[right] != target)
        return -1;
    return right;
}
```

### 滑动窗口解题框架：

```java
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0; 
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
```

### 股票题目 动态规划：

``` python 
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        '''
        状态转移方程  dp！第i天，还能操作k次，1：有股票，0：没股票
        dp_table[i][k][1] = max(dp_table[i-1][k][1], dp_table[i-1][k-1][0] - prices[i])
        dp_table[i][k][0] = max(dp_table[i-1][k][0], dp_table[i-1][k][1] + prices[i])
        注意 base case 和 怎么处理k
        '''
        n = len(prices)
        if n == 0: return 0
        # dp_table = [[0] * 2 for i in range(n)] #取消了一个数组
        for i in range(0,n):
            if i == 0:
                # dp_table[0][1] = -prices[i]
                # dp_table[0][0] = 0
                # 节约内存写法：
                dp_i_1 = -prices[i]
                dp_i_0 = 0
                
            else:
                temp = dp_i_1
                dp_i_1 = max(dp_i_1,0-prices[i])
                dp_i_0 = max(dp_i_0,temp+prices[i])
        # print(dp_table)
        return dp_i_0
```

### 动态规划 三大要素：

1. 重叠子问题

2. 最优子结构

   一个最优策略的子策略也是最优的。

3. 状态转移方程

**但反过来，最优子结构性质作为动态规划问题的必要条件，一定是让你求最值的**，以后碰到那种恶心人的最值题，思路往动态规划想就对了，这就是套路。

动态规划不就是从最简单的 base case 往后推导吗，可以想象成一个链式反应，不断以小博大。但只有符合最优子结构的问题，才有发生这种链式反应的性质。

找最优子结构的过程，其实就是证明状态转移方程正确性的过程，方程符合最优子结构就可以写暴力解了，写出暴力解就可以看出有没有重叠子问题了，有则优化，无则 OK。这也是套路，经常刷题的朋友应该能体会。