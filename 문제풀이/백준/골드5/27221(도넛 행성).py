import sys, collections
input = sys.stdin.readline

D = [(1,0),(0,1),(-1,0),(0,-1)]

def donuts_explore(i,j):
    queue = collections.deque()
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        for dx, dy in D:
            nx, ny = (x+dx) % N, (y+dy) % M
            if not visited[nx][ny] and not planet[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1
    return

N,M = map(int,input().split())
planet = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
donuts = []
cnt = 0
for i in range(N):
    for j in range(M):
        if planet[i][j] or visited[i][j]:
            continue
        else:
            donuts_explore(i,j)
            cnt += 1
print(cnt)