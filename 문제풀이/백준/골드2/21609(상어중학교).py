from collections import deque

def groupping():
    groups = dict()
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mapp[i][j] >= 1 and not visited[i][j]:
                visited[i][j] = 1
                queue = deque([(i,j)])
                group = set()
                group.add((i,j))
                block_num = mapp[i][j]
                rainbow_b = 0
                local_visited = [[0]*N for _ in range(N)]
                while queue:
                    x,y = queue.popleft()
                    for dx, dy in D:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < N and not local_visited[nx][ny]:
                            local_visited[nx][ny] = 1
                            if mapp[nx][ny] == block_num:
                                group.add((nx,ny))
                                queue.append((nx,ny))
                                visited[nx][ny] = 1
                            elif mapp[nx][ny] == 0:
                                group.add((nx,ny))
                                queue.append((nx,ny))
                                rainbow_b += 1
                group = sorted(list(group))
                if len(group) < 1:
                    continue
                for x,y in group:
                    if mapp[x][y] > 0:
                        standard_block = (x,y)
                        break
                key = (len(group), rainbow_b, standard_block[0], standard_block[1])
                groups[key] = group
    return groups

def gravity():
    for j in range(N):
        idx = N-1
        empty = 0
        while idx >= 0:
            if mapp[idx][j] == -1:
                empty = 0
            elif mapp[idx][j] == -2:
                empty += 1
            elif mapp[idx][j] >= 0:
                mapp[idx+empty][j], mapp[idx][j] = mapp[idx][j], mapp[idx+empty][j]
            idx -= 1
    return

def rotate():
    new_mapp = [[-2]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_mapp[(N-1)-j][i] = mapp[i][j]
    return new_mapp

N,M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
score = 0
D = [(1,0),(0,1),(-1,0),(0,-1)]
while True:
    groups = groupping()
    a = list(groups.keys())
    a.sort(key = lambda x : (x[0],x[1],x[2],x[3]))
    if len(a) < 1:
        break
    max_group = groups[a[-1]]
    if len(max_group) < 2:
        break
    for i,j in max_group:
        mapp[i][j] = -2
    score += len(max_group)**2
    gravity()
    mapp = rotate()
    gravity()
print(score)

# def bfs(i,j):
#     global visited
#     visited[i][j] = 1
#     queue = deque((i,j))
#     group = []
#     block_num = mapp[i][j]
#     rainbow_b = 0
#     while queue:
#         x,y = queue.popleft()
#         for dx, dy in D:
#             nx, ny = x+dx, y+dy
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 if mapp[nx][ny] == block_num:
#                     group.append((nx,ny))
#                     visited[nx][ny] = 1
#                 elif mapp[nx][ny] == 0:
#                     group.append((nx,ny))
#                     rainbow_b += 1
#     return group, rainbow_b