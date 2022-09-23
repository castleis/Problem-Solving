import sys
sys.stdin = open('input/5188.txt')

def solve(x,y,s):
    global minS
    s += arr[x][y]
    if s > minS:
        return
    if x == N-1 and y == N-1:
        if s < minS:
            minS = s
        return
    d = [(1,0),(0,1)]
    for dx, dy in d:
        nx,ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            solve(nx,ny,s)
            visited[nx][ny] = 0
    
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    minS = 10 * (2*N-1)
    solve(0,0,0)
    print(f'#{t} {minS}')