N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-2):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
