from collections import deque

def is_zero():
    global walls
    while zeros:
        x,y = zeros.popleft()
        # print(f'===================== [{x},{y}] =====================')
        D = D_o if x % 2 else D_e
        V[x][y] = 1
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W:
                # print(f'==========[{nx},{ny}] =========')
                if maps[nx][ny] == 1:
                    walls += 1
                    # print(f'=========== wall + 1 : {walls}')
                elif maps[nx][ny] == 0 and not V[nx][ny]:
                    zeros.append((nx,ny))
                    V[nx][ny] = 1
                    # print(f'=========== zero')
def is_wall():
    global walls
    for x,y in structures:
        # print(f'=================== [{x},{y}] ==================')
        D = D_o if x % 2 else D_e
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                # print(f'======= [{nx},{ny}]')
                walls += 1

W,H = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(H)]
walls = 0
zeros = deque()
structures = deque()
V = [[0]*W for _ in range(H)]
for i in range(0,H,H-1):
    for j in range(0,W):
        if maps[i][j]:
            structures.append((i,j))
        else:
            zeros.append((i,j))
            V[i][j] = 1
for i in range(1,H-1):
    for j in range(0,W,W-1):
        if maps[i][j]:
            structures.append((i,j))
        else:
            zeros.append((i,j))
            V[i][j] = 1

D_o = [(-1,-1),(0,-1),(1,-1),(1,0),(0,1),(-1,0)]
D_e = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(0,-1)]
is_zero()
is_wall()
print(walls)