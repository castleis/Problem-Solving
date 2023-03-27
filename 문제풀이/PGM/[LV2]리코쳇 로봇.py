from collections import deque
def solution(board):
    N, M = len(board), len(board[0])
    D = [(1,0),(0,1),(-1,0),(0,-1)]

    def bfs(i,j):
        V = [[0]*M for _ in range(N)]
        queue = deque([(i,j)])
        V[i][j] = 1
        while queue:
            x,y = queue.popleft()
            if board[x][y] == 'G':
                return V[x][y]
            for dx, dy in D:
                nx, ny = x,y
                go = True
                while go:
                    nx, ny = nx+dx, ny+dy
                    if 0 <= nx < N and 0 <= ny < M:
                        print(nx,ny,board[nx][ny])
                        if board[nx][ny] == 'D':
                            nx -= dx
                            ny -= dy
                            go = False
                    elif nx < 0 or nx >= N or ny < 0 or ny >= M:
                        nx -= dx
                        ny -= dy
                        go = False
                if not V[nx][ny]:
                    V[nx][ny] = V[x][y] + 1
                    queue.append((nx,ny))         
        return -1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                cnt = bfs(i,j)
                return cnt-1 if cnt > 0 else cnt
board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))