N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
cnt = 0
stack = [1]
visited = [0]*(N+1)
visited[1] = 1
while stack:
    n = stack.pop()
    for m in arr[n]:
        if not visited[m]:
            stack.append(m)
            visited[m] = 1
            cnt += 1
print(cnt)