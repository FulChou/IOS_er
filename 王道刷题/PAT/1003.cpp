// 单源最短路径 + 有优先级的；

#include<iostream>
#include<vector>
#include<queue>

using namespace std;

const int MAX = 99999999;
// 

int Map[510][510];

void Dijkstra(int Map[][510],int S,int n ,vector<int> &d, int weight[],int D){ 
    int w[510];
    int num[510];
    // initial:
    w[S] = weight[S];
    num[S] = 1;
    
    vector<bool> isVisit; //(n,false); //初始化大小和值：
    //vector<int> d; // d for S
    // 初始化 isVisit:
    //fill(isVisit,isVisit,false);

    for (int i = 0; i < n; i++)
    {
        isVisit.push_back(false);
        d.push_back(MAX);
    }
    // 必须在 放完极大之后，然后让源点dis = 0；
    d[S] = 0;
    // initial d:  从S开始算，不需要自己去初始化d,设为MAX就行。
    // for(int i=0;i<n;i++){
    //     if(Map[S][i])
    //     d[i] = Map[S][i];
    // }
    //isVisit[S] = true;
    //d[S] = 0;

    // 找到当前离 S 最近的点：， 第一个本身：
    for (int i = 0; i < n; i++)
    {
        int index = -1;
        int MinD = MAX;
        // 找到最小的 distence  index and value;
        for (int j = 0; j < n; j++)
        {
            if(isVisit[j] == false && d[j]<MinD){
                index = j;
                MinD = d[j];
            }
        }
        if(index == -1) return ;// 说明剩下的点不与起点连同；

        isVisit[index] = true; // 加入到已经访问数组中。
       
        for (int v = 0; v < n; v++) // 更新其他点的坐标：
        {
            if(isVisit[v] == false && Map[index][v]!=MAX){ // 没有访问过，并且存在一条 index to v的边
                if(d[index]+ Map[index][v] < d[v]){
                    d[v] = d[index]+ Map[index][v]; // 更新 d 数组
                    num[v] = num[index]; // 更新 有多个路径的数组
                    w[v] = w[index] + weight[v]; // update  路线权重，s to v = s自己+v；
                }else if(d[index] + Map[index][v] == d[v]){
                    num[v] = num[v] + num[index];
                    if(w[index] + weight[v] > w[v]){
                        w[v] = w[index] + weight[v];
                    }
                }

            }
            
        }
    }
    printf("%d %d",num[D],w[D]);

}

void BFS(int Map[][510],int S,int n){
    queue<int> q;
    q.push(S); // 放入源点：
    //  已经访问过的点：
    vector<bool> visit;
    for (int i = 0; i < n; i++)
    {
        visit.push_back(false);
    }
    visit[S] = true;

    int index;
    while (!q.empty())
    {
        index = q.front(); //拿出第一个点：
        q.pop();
        for(int j=0;j<n;j++){
            if(Map[index][j]<MAX && !visit[j]){
                visit[j] = true;
                cout<<""<<j<<endl;
                q.push(j);
            }
        }
    }

}


int main(){

    int N,M,C1,C2;
    cin>>N>>M>>C1>>C2;
    int weight [N]; // 读入每个city的people；
    for (int i = 0; i < N; i++)
    {
        cin>>weight[i];
    }

    // initial map
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            Map[i][j] = MAX;
        }
        
    }
    
    // 构建地图
    for (int i = 0; i < M; i++)
    {
        int x,y,length;
        cin>>x>>y>>length;
        Map[x][y] = length;
        Map[y][x] = length; // 双向表：
    }

    // dijsktra:
    vector<int> d; // distance matrix;
    //Dijkstra(Map,C1,N,d);
    //BFS(Map,C1,N);
    Dijkstra(Map,C1,N,d,weight,C2);

    return 0;
}