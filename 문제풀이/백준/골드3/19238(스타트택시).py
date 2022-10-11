from collections import deque, defaultdict

def start(X,Y):
    global F
    if 2 <= mapp[X][Y] <= 2+M:
        # print(f'xortl!~~!~! {mapp[X][Y]+1000}')
        return end(X,Y)
    queue = deque()
    queue.append((X,Y))
    visited = [[0]*N for _ in range(N)]
    visited[X][Y] = 1
    while queue:   
        order = []
        F -= 1
        if F < 0 :
            return False
        # print(f'=================현재 연료 : {F}====================')
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for dx,dy in d:
                nx,ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if mapp[nx][ny] == 1:
                        continue
                    visited[nx][ny] = visited[x][y] + 1
                    if 2 <= mapp[nx][ny] <= M+2:
                        # print(f'목적지로 ~~~~ [{nx},{ny}]')
                        order.append((nx,ny))
                    queue.append((nx,ny))
        # print(visited)
        if order:
            x,y = sorted(order)[0]
            return end(x,y)
    return False

def end(X,Y):
    global F
    # print('end')
    queue = deque()
    queue.append((X,Y))
    EX,EY = quest[(X,Y)]
    print(f'목적지 : [{EX},{EY}]')
    visited = [[0]*N for _ in range(N)]
    visited[X][Y] = 1
    mapp[X][Y] = 0
    while queue:
        F -= 1
        if F < 0:
            return False
        # print(f'==========={F}===========')
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for dx,dy in d:
                nx,ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    # print(nx,ny, mapp[nx][ny])
                    if mapp[nx][ny] == 1:
                        continue
                    visited[nx][ny] = visited[x][y] + 1
                    if nx == EX and ny == EY:
                        # print(f'도착지 연료 : {F}, 사용한 연료 : {visited[nx][ny]-1}')
                        return visited[nx][ny]-1, nx, ny
                    queue.append((nx,ny))
    return False

N,M,F = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
X,Y = map(int,input().split())
quest = defaultdict(list)
for i in range(2,M+2):
    sx,sy,ex,ey = map(int,input().split())
    mapp[sx-1][sy-1] = i
    quest[(sx-1,sy-1)] += (ex-1,ey-1)
# print(mapp, quest)
d = [(-1,0),(0,-1),(0,1),(1,0)]
X -= 1
Y -= 1
for _ in range(M):
    # print()
    # print(f'택시 출발 : {X},{Y}')
    ans = start(X,Y)
    # print(ans)
    if ans == False:
        F = -1
        break
    F += ans[0]*2
    # print(f'Fuel : {F}')
    X,Y = ans[1],ans[2]
print(F)

'''
7 15 9
0 0 0 1 0 0 0
0 0 0 0 1 0 0
0 0 0 0 0 0 0
0 0 1 0 0 0 0
0 1 0 0 1 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
5 6
1 2 2 3
7 3 5 7
3 3 5 6
6 6 3 3
5 6 5 7
4 5 7 3
2 2 3 6
4 4 2 2
7 4 4 7
1 5 6 1
6 2 4 1
1 7 6 1
3 4 5 7
4 2 1 5
4 1 6 3
'''