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

# bellman ford算法
def main():
    n,m = map(int,input().split())
    edges = []
    for _ in range(m):
        s,e,val = map(int,input().split())
        edges.append([s,e,val])

    mindist = [float('inf')] * (n + 1)
    mindist[1] = 0
    
    for _ in range(n - 1):
        update = False
        for s,e,val in edges:
            if mindist[s] != float('inf') and mindist[e] > mindist[s] + val:
                update = True
                mindist[e] = mindist[s] + val

        if not update:
            break
    
    if mindist[n] == float('inf'):
        print('unconnected')
    else:
        print(mindist[n])

# SPFA 算法
from collections import defaultdict

def main():
    n,m = map(int,input().split())
    mapper = defaultdict(list)
    for _ in range(m):
        s,e,val = map(int,input().split())
        mapper[s].append([e,val])

    # 记录最小距离
    mindist = [float('inf')] * (n + 1)
    # 记录是否已经在队列里，不需要重复添加
    visited = [False] * (n + 1)
    queue = []
    mindist[1] = 0
    queue.append(1)
    visited[1] = True
    
    while queue:
        cur = queue.pop(0)
        visited[cur] = False
        for e,val in mapper[cur]:
            if mindist[e] > mindist[cur] + val:
                mindist[e] = mindist[cur] + val
                if not visited[e]:
                    visited[e] = True
                    queue.append(e)
    
    if mindist[n] == float('inf'):
        print('unconnected')
    else:
        print(mindist[n])
