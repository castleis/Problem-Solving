import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
# 배지가 영어인줄 알았는데 한자어네 @.@
bage = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
d = [(1,0),(-1,0),(0,1),(0,-1)]

virus = deque()
visited = [[0]*N for _ in range(N)]

for k in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if bage[i][j] == k:
                virus.append((i,j))
                visited[i][j] = 1
print(visited)
print(bage)
print(virus)
while S:
    print(f'========================== {S}초 ===========================')
    for i in range(len(virus)):
        print(f'================ {i}번째 번식 ==================')
        x,y = virus.popleft()
        virus_num = bage[x][y]
        for dx,dy in d:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                if not visited[x+dx][y+dy]:
                    if bage[x+dx][y+dy] == 0:
                        virus.append((x+dx,y+dy))
                        bage[x+dx][y+dy] = virus_num
                        visited[x+dx][y+dy] = 1
        print(f'bage : {bage}')
        print(f'stack : {virus}')
    S -= 1
print(bage[X-1][Y-1])


# Solution
def solution():
    n, k = map(int, input().split())
    maps = [(list(map(int, input().split()))) for _ in range(n)]
    s, x, y = map(int, input().split())

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x -= 1
    y -= 1
    if maps[x][y] != 0 :
        print(maps[x][y])
        return
    
    q = []
    # Wow-point : (x,y)부터 방문쓰;;
    visited = [(x, y)]
    maps[x][y] = 1001
    for i in range(s):
        temp = []
        while visited:
            x, y = visited.pop()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if nx > -1 and ny > -1 and nx < n and ny < n:
                    # 0 or 1001 이 아니라면 q에 넣어주기 : 바이러스가 이미 있는 곳
                    if maps[nx][ny] != 0 and maps[nx][ny] != 1001:
                        q.append(maps[nx][ny])
                    # 0이라면 temp에 넣어주기
                    elif maps[nx][ny] == 0:
                        temp.append((nx, ny))
                    # 새로 방문한 곳은 1001로 바꿔줌
                    maps[nx][ny] = 1001
        # temp를 visited에 넣어주기(슬라이싱으로 복사)
        visited = temp[:]
        if q :
            # 어차피!! 여러 바이러스가 있으면 제일 낮은 번호가 전염되기 때문
            print(min(q))
            return
    if not q :
        print(0)

solution()
