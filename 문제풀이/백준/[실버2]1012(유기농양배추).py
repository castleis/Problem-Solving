import sys
input = sys.stdin.readline

d = [(1,0),(-1,0),(0,1),(0,-1)]
def find(check,b,a):
    stack = [(b,a)]
    while stack:
        y,x = stack.pop()
        for dy,dx in d:
            if 0 <= y+dy < N and 0 <= x+dx < M:
                if check[y+dy][x+dx]:
                    check[y+dy][x+dx] = 0
                    stack.append((y+dy,x+dx))
    return

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    check = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x,y = map(int,input().split())
        check[y][x] = 1

    for x in range(M):
        for y in range(N):
            if check[y][x]:
                find(check,y,x)
                cnt += 1

    print(cnt)