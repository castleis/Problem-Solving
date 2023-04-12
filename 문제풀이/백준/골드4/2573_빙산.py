from collections import deque

def is_range(x,y):
    if 0 <= x < row and 0 <= y < col:
        return True
    return False

def melting(i,j):
    melt_dict = dict()
    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        for dx, dy in directions:
            nx,ny = x+dx, y+dy
            if is_range(nx,ny) and not visited[nx][ny]:
                if sea[nx][ny] == 0:
                    if (x,y) in melt_dict.keys():
                        melt_dict[(x,y)] += 1
                    else:
                        melt_dict[(x,y)] = 1
                else:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    for key,value in melt_dict.items():
        x,y = key
        sea[x][y] = sea[x][y]-value if sea[x][y]-value > 0 else 0
    return

def dfs(x,y):
    for dx, dy in directions:
        nx,ny = x+dx, y+dy
        if is_range(nx,ny) and not group_visited[nx][ny]:
            if sea[nx][ny] > 0:
                group_visited[nx][ny] = 1
                dfs(nx,ny)
    return

row, col = map(int,input().split())
sea = [list(map(int,input().split())) for _ in range(row)]
directions = [(1,0),(0,1),(-1,0),(0,-1)]
ices = []
for i in range(row):
    for j in range(col):
        if sea[i][j] > 0:
            ices.append((i,j))

year = 0
while True:
    
    visited = [[0]*col for _ in range(row)]
    for i,j in ices:
        if sea[i][j] > 0 and not visited[i][j]:
            melting(i,j)

    group_cnt = 0
    group_visited = [[0]*col for _ in range(row)]
    for i,j in ices:
        if sea[i][j] > 0 and not group_visited[i][j]:
            dfs(i,j)
            group_cnt += 1
    year += 1
    if group_cnt > 1:
        break
print(year)

'''
5 5
0 0 0 0 0
0 0 9 0 0
0 0 3 1 0
0 0 9 0 0
0 0 0 0 0
'''