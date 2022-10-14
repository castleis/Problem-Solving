import sys
sys.stdin = open('input/2117.txt')

pay = [k**2 + (k-1)**2 for k in range(26)]
# print(pay)

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    mapp = [list(map(int,input().split())) for _ in range(N)]

    # 집 찾기
    homes = []
    for i in range(N):
        for j in range(N):
            if mapp[i][j]:
                homes.append((i,j))
    max_profit = 0
    for k in range(1,N+5):
        for x in range(N):
            for y in range(N):
                home_cnt = 0
                for i,j in homes:
                    if abs(x-i) + abs(y-j) <= k:
                        if mapp[x-i][y-j] or mapp[i-x][y-j] or mapp[x-i][j-y] or mapp[i-x][j-y]:
                            home_cnt += 1

                if home_cnt * M >= pay[k]:
                    if max_profit < home_cnt * M - pay[k]:
                        ans = home_cnt

    print(f'#{tc} {ans}')