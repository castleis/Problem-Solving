'''
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
출력
1 2 3 4 5 7 6
'''

def bfs(graph,start):
    # 시작정점을 큐에 넣어주고 시작
    queue = [start]
    visited[start] = 1

    while queue:
        # 현재 제일 앞에 있는 원소를 pop, 출력
        v = queue.pop(0)
        print(v)
        # 인접한 정점들 중 방문하지 않은 정점이 있다면 큐에 넣어주고 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

n,m = map(int,input().split())
arr = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
# graph 만들어주기
for i in range(m):
    graph[arr[2*i]].append(arr[2*i+1])
    graph[arr[2*i+1]].append(arr[2*i])

# 1부터 bfs탐색 시작
bfs(graph,1)

