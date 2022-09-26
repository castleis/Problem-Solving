from collections import deque
def escape():
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        i,j,w = q.popleft()
        for di,dj in d:
            ni,nj = i+di, j+dj
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and forest[ni][nj] != 'X':
                if forest[ni][nj] == 'D':
                    if w == 0:
                        return visited[i][j]
                    else: continue
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj,w))
    return 'KAKTUS'

R,C = map(int,input().split())
forest = [list(input()) for _ in range(R)]
q = deque()
visited = [[0]*(C) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            si,sj = i,j
            visited[i][j] = 1
        elif forest[i][j] == '*':
            q.append((i,j,1))
            visited[i][j] = 1
q.append((si,sj,0))
print(escape())