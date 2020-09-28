/*
构造一棵树， 树的层序遍历；
树的 抽象数据结构很重要
根据 层数来确定每一个值；
*/
#include<iostream>
#include<queue>

using namespace std;

const int MAX_SIZE = 110;

struct Node{
    //int data;
    int parent ;
    Node(){
        parent = -1;
    }
};

struct Tree{
    Node nodes[MAX_SIZE];
    int n;
};
// 层序遍历树：
void levelOrder(Tree tree){
    queue<int> q;
    q.push(1);
    int num[tree.n+1];
    while (!q.empty())
    {
        int root = q.front();//
        q.pop();
        num[root] = 1;// 默认 没有儿子节点
        for (int i = 1; i <= tree.n; i++) // 算出来每一个节点是不是 叶子节点：
        {
            if(tree.nodes[i].parent == root){
                num[root] = 0;
                q.push(i); //子节点加入队列
            }
        }
        
    }
    //
    int result[tree.n+1];
    fill(result,result+tree.n+1,0);// initial 0;
    
    int maxLevel = 0; 
    for (int i = 1; i < tree.n+1; i++)
    {
        int index = tree.nodes[i].parent;
        int level = 0;
        while (index != -1){
            index = tree.nodes[index].parent;
            level++;
        }
        if(level>maxLevel) maxLevel = level; // 计算出最大层数；
        result[level] += num[i];
    }
    // output:
    bool flag = true;
    for (int i = 0; i <= maxLevel; i++) // 输出的层数不对：不一定有 n层
    {   
        if(flag) {
            cout<<result[i];
            flag = false;
        }else cout<<" "<<result[i];
    }
    
    

}

int main(){
    Tree tree;
    int n,m;
    cin>>n>>m;
    tree.n = n;
    for (int i = 0; i < m; i++)
    {
        int parent,k;
        cin>>parent>>k;
        for (int j = 0; j < k; j++)
        {   
            int chird;
            scanf("%02d",&chird); // 指定字符的占位；很重要!
            //cin>>chird;
            //cout<<chird;
            tree.nodes[chird].parent = parent;
        }
        
    }
    // 层序遍历：
    levelOrder(tree);
    

    return 0;
}

/*
6 2
01 2 02 03
02 3 04 05 06
*/