import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort()

visited = [0]*(N+1)
visited[R] = 1
depth = 1
def dfs(x):
    global depth
    # if visited[x]:
    #     return
    for neig in graph[x]:
        if not visited[neig]:
            depth += 1
            visited[neig] = depth
            dfs(neig)

dfs(R)
for i in range(1,N+1):
     print(visited[i])