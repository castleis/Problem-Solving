from collections import deque

def bfs():
    queue = deque()
    queue.append(a)
    visited = [-1]*100001
    visited[a] = 0
    while queue:
        now = queue.popleft()
        jump = bridges[now]
        for i in range(now, N+1, jump):
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i == b:
                    return visited[i]
        for i in range(now, 0, -jump):
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i == b:
                    return visited[i]
    return -1

N = int(input())
bridges = [0] + list(map(int,input().split()))
a,b = map(int,input().split())
print(bfs())