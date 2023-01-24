from collections import deque
import sys
input = sys.stdin.readline
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(int(input())):
    H, W = map(int, input().split())
    mapp = [list(input()) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    sheeps = deque()
    cnt = 0
    for i in range(H):
        for j in range(W):
            if mapp[i][j] == '#' and not visited[i][j]:
                sheeps.append((i, j))
                visited[i][j] = 1
                cnt += 1
                while sheeps:
                    si, sj = sheeps.popleft()
                    for di, dj in delta:
                        ni, nj = si+di, sj+dj
                        if 0 <= ni < H and 0 <= nj < W:
                            if mapp[ni][nj] == '#' and not visited[ni][nj]:
                                sheeps.append((ni, nj))
                                visited[ni][nj] = 1
            elif mapp[i][j] == '.':
                visited[i][j] = 1
                continue
    print(cnt)