from collections import deque
import sys
input = sys.stdin.readline

# def in_range(x,y,dx,dy,nx,ny):
#     if dx in [1,0,-1]:
#         if x - x%R <= nx < x + (R - x%R) and 0 <= ny < C:
#             return True
#     else:
#         if 0 <= nx < L*R and 0 <= ny < C:
#            return True
#     return False

def bfs(x,y,z):
    V = [[[0]*C for _ in range(R)] for _ in range(L)]
    queue = deque()
    queue.append((x,y,z))
    V[x][y][z] = 1
    while queue:
        x,y,z = queue.popleft()
        for dx, dy, dz in D:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if not V[nx][ny][nz]:
                    if maps[nx][ny][nz] == '#':
                        V[nx][ny][nz] = True
                        continue
                    elif maps[nx][ny][nz] == '.':
                        queue.append((nx,ny,nz))
                        V[nx][ny][nz] = V[x][y][z] + 1
                    elif maps[nx][ny][nz] == 'E':
                        return V[x][y][z]
    return False

def solve():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if maps[i][j][k] == 'S':
                    ans = bfs(i,j,k)
                    if ans == False:
                        return 'Trapped!'
                    else:
                        return f'Escaped in {ans} minute(s).'
while True:
    L,R,C = map(int,input().split())
    if L + R + C == 0:
        break
    D = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]
    maps = []
    for _ in range(L):
        _map = [list(input()) for _ in range(R)]
        blank = input()
        maps.append(_map)
    print(solve())