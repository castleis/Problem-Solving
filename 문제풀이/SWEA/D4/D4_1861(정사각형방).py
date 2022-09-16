import sys
sys.stdin = open('input/1861.txt')

def visit():
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    maxx = 0
    ans = (0,0)
    for x in range(N):
        for y in range(N):
            cnt = 0
            visited = [[0]*N for _ in range(N)]
            visited[x][y] = 1
            stack = [(x,y)]

            while stack:
                i,j = stack.pop()
                cnt += 1
                for di,dj in d:
                    ni,nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                        if room[ni][nj] == room[i][j] + 1:
                            stack.append((ni,nj))
                            visited[ni][nj] = 1
            if cnt > maxx:
                maxx = cnt
                ans = (room[x][y],maxx)
            elif cnt == maxx:
                if room[x][y] < ans[0]:
                    ans = (room[x][y], maxx)
    return ans

T = int(input())
for t in range(1,T+1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int,input().split())))
    ans = visit()
    print(f'#{t} {ans[0]} {ans[1]}')