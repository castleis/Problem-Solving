def solve(x,y):
    global flag
    # 봉우리는, 주변 값들이 자신보다 작을 때.
    visited[x][y] = 1
    now = farm[x][y]
    for dx, dy in delta:
        nx,ny = x+dx,y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if farm[nx][ny] > now:      # 주변보다 작으면 산봉우리가 아님
                flag = False
            if not visited[nx][ny] and farm[nx][ny] == now:     # 같은 높이를 찾아서 dfs
                    solve(nx,ny)

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
farm = [list(map(int,input().split())) for _ in range(N)]
delta = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
visited = [[0]*M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            flag = True     # 산봉우리임을 가정하고 시작!
            solve(i,j)
            if flag:
                cnt += 1
print(cnt)