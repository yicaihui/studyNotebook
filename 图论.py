# dijkstra 算法 两个for循环
def main():
    N,M = map(int,input().split())
    records = []
    for _ in range(M):
        records.append(map(int,input().split()))
    
    # 邻接矩阵或邻接表
    grid = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for S,E,V in records:
        grid[S][E] = V

    # 记录某个节点距离源点的最短距离
    mindists = [float('inf')] * (N + 1)
    mindists[1] = 0
    # 记录是否访问过
    visited = [False] * (N + 1)

    # parents记录路径
    parents = [-1] * (N + 1)

    for _ in range(N):
        cur = -1
        mindist = float('inf')
        for i in range(1,N + 1):
            if not visited[i] and mindists[i] < mindist:
                cur = i
                mindist = mindists[i]
        
        if cur == -1:
            break
        
        visited[cur] = True

        for j in range(1, N + 1):
            if not visited[j] and mindists[j] > mindists[cur] + grid[cur][j]:
                mindists[j] = mindists[cur] + grid[cur][j]
                parents[j] = cur

    if mindists[N] == float('inf'):
        print(-1)
    else:
        print(mindists[N])

# dijkstra 堆优化版
from collections import defaultdict
import heapq

def main():
    N,M = map(int,input().split())
    records = []
    for _ in range(M):
        records.append(map(int,input().split()))
    
    # 邻接矩阵或邻接表
    mapper = defaultdict(list)
    for s,e,val in records:
        mapper[s].append([e,val])

    # 记录某个节点距离源点的最短距离
    mindists = [float('inf')] * (N + 1)
    mindists[1] = 0
    # 记录是否访问过
    visited = [False] * (N + 1)
    # 初始化优先队列
    # 添加元组(priority, value)
    pq = []
    heapq.heappush(pq,(0,1))

    while pq:
        dist,cur = heapq.heappop(pq)
        
        if visited[cur]:
            continue

        visited[cur] = True

        for e,val in mapper[cur]:
            if not visited[e] and mindists[e] > dist + val:
                mindists[e] = dist + val
                heapq.heappush(pq,(mindists[e],e))

    if mindists[N] == float('inf'):
        print(-1)
    else:
        print(mindists[N])

# bellman ford算法 + 判断负权回路
def main():
    n,m = map(int,input().split())
    edges = []
    for _ in range(m):
        s,t,v = map(int,input().split())
        edges.append([s,t,v])
 
    mindists = [float('inf')] * (n + 1)
    flag = False
 
    mindists[1] = 0
 
    for i in range(1,n + 1):
        update = False
        for s,t,v in edges:
            if mindists[s] != float('inf') and mindists[t] > mindists[s] + v:
                mindists[t] = mindists[s] + v
                update = True
        if i == n and update:
            flag = True
        elif i != n and not update:
            break
 
    if flag:
        print('circle')
    elif mindists[n] == float('inf'):
        print('unconnected')
    else:
        print(mindists[n])

# SPFA 算法
from collections import defaultdict
def main():
    n,m = map(int,input().split())
    mapper = defaultdict(list)
    for _ in range(m):
        s,t,v = map(int,input().split())
        mapper[s].append([t,v])
 
    mindists = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    counts = [0] * (n + 1)
    queue = []
    flag = False
 
    mindists[1] = 0
    visited[1] = True
    queue.append(1)
 
    while queue:
        s = queue.pop(0)
        visited[s] = False
        for t,v in mapper[s]:
            if mindists[t] > mindists[s] + v:
                mindists[t] = mindists[s] + v
                if not visited[t]:
                    visited[t] = True
                    queue.append(t)
                    counts[t] += 1
                    if counts[t] == n:
                        flag = True
        if flag:
            break
 
    if flag:
        print('circle')
    elif mindists[n] == float('inf'):
        print('unconnected')
    else:
        print(mindists[n])
