from collections import deque
M,N = map(int,input().split())
walls = [list(map(int,input())) for _ in range(M)]
D = [(1,0),(0,1),(-1,0),(0,-1)]

def is_united(x,y):
    # 체크용 x,y에서부터 bfs, 방문처리
    queue = deque()
    queue.append((x,y))
    visited = [[0]*N for _ in range(M)]
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in D:
            nx, ny = x+dx, y+dy
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and walls[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    # 0이 아닌데(곰팡이가 있는대) 방문하지 않았다는 것은 한 덩어리가 되지 않았다는 뜻 아닌가????? ㅡㅡ
    for i in range(M):
        for j in range(N):
            if walls[i][j] > 0 and not visited[i][j]:
                return False
    return True

def solve():
    # queue에 곰팡이 담기
    queue = deque()
    for i in range(M):
        for j in range(N):
            if walls[i][j] != 0:
                queue.append((i,j,walls[i][j]))
    # 확인은 거꾸로 하려고 마지막번째 담음
    day = 0
    check_x, check_y = queue[-1][0],queue[-1][1]
    # 0일차 확인
    if is_united(check_x, check_y):
        return day

    # 1일 단위로 bfs를 돌아줌니다
    while queue:
        day += 1
        for _ in range(len(queue)):
            x,y,s = queue.popleft()
            for dx in range(-s,s+1):
                for dy in range(-s,s+1):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if walls[nx][ny] < s:
                            walls[nx][ny] = s
                            queue.append((nx,ny,walls[nx][ny]))
        # 다음날로 넘어가기 전에 한 덩어리가 되었는지 체크
        if is_united(check_x, check_y):
            return day
print(solve())