import sys
sys.stdin = open('input/2117.txt')

pay = [k**2 + (k-1)**2 for k in range(21)]
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
    # print(homes)
    result = [0]*N
    for k in range(3,4):
        for i,j in homes:
            cnt = 0
            for x in range(-k,k):
                for y in range(-(k-x), k-x):
                    if 0 <= i+x < N and 0 <= j+y < N:
                        if mapp[i+x][j+y]:
                            cnt += 1
            # print(i,j,k,cnt)
            result[k] = max(result[k], cnt*M - pay[k])
    # print(result)
k = 3
i,j = 3,3
cnt = 0
for x in range(-k,k):
    print(f'=========={x}=============')
    for y in range(-(-k-x), (k+x)):
        cnt += 1
        print(x,y)
print(cnt)

# 마름모 만들기
