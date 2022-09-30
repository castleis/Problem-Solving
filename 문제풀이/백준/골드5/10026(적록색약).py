import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = [list(input()) for _ in range(N)]
visited1 = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
cnt1,cnt2 = 0,0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            q1 = deque()
            q1.append((i,j))
            visited1[i][j] = 1
            while q1:
                x,y = q1.popleft()
                color = arr[x][y]
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < N and not visited1[nx][ny] and arr[nx][ny] == color:
                        q1.append((nx,ny))
                        visited1[nx][ny] = 1
            cnt1 += 1
        if not visited2[i][j]:
            q2 = deque()
            q2.append((i,j))
            visited2[i][j] = 1
            while q2:
                x,y = q2.popleft()
                color = arr[x][y]
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny]:
                        if color == 'G' or color == 'R':
                            if arr[nx][ny] in 'GR':
                                q2.append((nx,ny))
                                visited2[nx][ny] = 1
                        else:
                            if arr[nx][ny] == color:
                                q2.append((nx,ny))
                                visited2[nx][ny] = 1
            cnt2 += 1
print(cnt1, cnt2)
