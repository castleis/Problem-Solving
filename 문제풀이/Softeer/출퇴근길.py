import sys
sys.setrecursionlimit(10 ** 6)

def dfs(s, graph, visited):
    if visited[s]:
        return
    visited[s] = 1
    for node in graph[s]:
        dfs(node, graph, visited)
    return

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

S,T = map(int,input().split())

from_S = [0]*(n+1)
from_S[T] = 1
dfs(S,graph,from_S)

from_T = [0]*(n+1)
from_T[S] = 1
dfs(T,graph,from_T)

To_S = [0]*(n+1)
dfs(S,reverse_graph,To_S)

To_T = [0]*(n+1)
dfs(T,reverse_graph,To_T)

count = 0
for i in range(1,n+1):
    if from_S[i] == from_T[i] == To_S[i] == To_T[i] == 1:
        count += 1
print(count-2)