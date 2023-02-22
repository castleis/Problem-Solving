from collections import deque

def solution(maps):
    def bfs(x,y,target):
        V = [[0]*M for _ in range(N)]
        queue = deque()
        queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M:
                    if maps[nx][ny] != 'X' and not V[nx][ny]:
                        queue.append((nx,ny))
                        V[nx][ny] = V[x][y] + 1
                    if maps[nx][ny] == target:
                        return nx,ny, V[nx][ny]
        return -1
    M = len(maps[0])
    N = len(maps)
    D = [(1,0),(0,1),(-1,0),(0,-1)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                result = bfs(i,j,'L')
                if result != -1:
                    result1 = bfs(result[0],result[1],'E')
                    if result1 != -1:
                        answer = result[2] + result1[2]
                    else:
                        answer = -1
                else:
                    answer = -1
                return answer

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))
maps1 = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
print(solution(maps1))