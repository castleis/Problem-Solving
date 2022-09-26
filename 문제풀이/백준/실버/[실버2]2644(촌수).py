import sys
input = sys.stdin.readline
'''
간선의 갯수를 구해야 하는 걸까~~~ 구한다면 어떻게 구해야하는 걸까~~~
DFS로 구하는것이 어떨까!
'''
N = int(input())
a,b = map(int,input().split())
m = int(input())

graph = [[]for _ in range(N+1)]
for _ in range(m):
    p,c = map(int,input().split())
    graph[p].append(c)
    graph[c].append(p)

print(graph)
visited = [0]*(N+1)
result = []

def DFS(v,depth):
    depth += 1
    visited[v] = 1
    print(f'{v} : {depth}')
    print(f'{v} : {visited}')
    if v == b:
        
        result.append(depth)

    for i in graph[v]:
        if not visited[i]:
            print(f'recursive! : {i}')
            DFS(i,depth)
DFS(a,0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)


# 씁쓸.... 나는 말하는 감자인가보다!!