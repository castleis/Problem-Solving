from collections import deque
import sys
input = sys.stdin.readline
def hunt(x,y,size,cnt):
    q = deque()
    visited = [[0]*N for _ in range(N)]
    q.append((x,y))
    visited[x][y] = 1
    offering = []
    eating_time = 1000000
    while q:
        x,y = q.popleft()
        # print(f'=============[{x},{y}]=============')
        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if sea[nx][ny] > size:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                if offering and visited[nx][ny] > eating_time:
                    continue
                # 먹을 수 있는 물고기를 만나면!!!!!!!!!!!
                if 0 < sea[nx][ny] < size:
                    offering.append((nx,ny))
                    eating_time = visited[nx][ny]
                q.append((nx,ny))
    if not offering:
        return 0
    # offering.sort()
    fx,fy = sorted(offering)[0]
    sea[fx][fy] = 0
    cnt += 1
    t = visited[fx][fy] - 1
    if cnt == size:
        size += 1
        cnt = 0
    return t, size, cnt, fx, fy

N = int(input())
sea = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            x,y = i,j
            sea[x][y] = 0

time,cnt = 0,0
size = 2
while True:
    ans = hunt(x,y,size,cnt)
    if ans == 0:
        break 
    t,size,cnt,x,y = ans
    time += t

print(time)