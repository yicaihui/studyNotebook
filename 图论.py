def main():
    N,M = map(int,input().split())
    grid = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        S,E,V = map(int,input().split())
        grid[S][E] = V
    
    visited = [False] * (N + 1)
    mindist = [float('inf')] * (N + 1)
    mindist[1] = 0
    for _ in range(1,N + 1):
        cur = -1
        minval = float('inf')
        for i in range(1,N + 1):
            if not visited[i] and mindist[i] < minval:
                cur = i
                minval = mindist[i]
        # 如果没有找到合适的一点，提前结束循环
        if cur == -1:
            break
        visited[cur] = True
        # 更新距离
        for j in range(1, N + 1):
            if not visited[j] and mindist[j] > mindist[cur] + grid[cur][j]:
                mindist[j] = mindist[cur] + grid[cur][j]
    if mindist[N] == float('inf'):
        print('-1')
    else:
        print(mindist[N])


main()
