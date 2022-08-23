import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    visited = [[0]*M for _ in range(N)]
    # print(visited)
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    cnt = 0
    
    if K == 1:
        print(1)
        continue

    cabbage = []
    for _ in range(K):
        x,y = map(int,input().split())
        cabbage.append((x,y))
    while cabbage:
        x,y = cabbage.pop()
        print(f'새로운 곳 탐험!!! {y},{x}')
        if not visited[y][x]:
            visited[y][x] = 1
            cnt += 1
            print(f'cnt + 1 : ', cnt)

        for dy,dx in d:
            if 0 <= x+dx < M and 0 <= y+dy < N:
                if visited[y+dy][x+dx] == 0:
                    visited[y+dy][x+dx] = 1
        print(visited)
        # print(f'cnt : {cnt}')
    print(cnt)