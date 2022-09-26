from collections import deque

def solve(x,y,size,cnt):
    d = [(-1,0),(0,-1),(1,0),(0,1)]
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        t = 0
        print(f'=============[{x},{y}]=============')
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if 0 < sea[nx][ny] < size:
                    t += visited[nx][ny]-1
                    cnt += 1
                    print(f'먹는당 : [{nx},{ny}], {t}, {cnt}')
                    sea[nx][ny] = 0
                    if cnt >= size:
                        size += 1
                        print(f'벌크업!!! -> {size}')
                        cnt = 0
                    return t, size, cnt, nx, ny
                else:
                    q.append((nx,ny))
        print(visited)
    return 0

N = int(input())
sea = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            x,y = i,j
time,cnt = 0,0
size = 2

while True:
    print(f'===================================================')
    ans = solve(x,y,size,cnt)
    print(f'ans : {ans}')
    if ans == 0:
        break 
    t,size,cnt,x,y = ans
    time += t

print(time, size)
print(sea)