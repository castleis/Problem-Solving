import sys
sys.stdin = open('6485.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ab = []
    for _ in range(N):
        ab.append(list(map(int,input().split())))
    P = int(input())
    c = []
    for _ in range(P):
        c.append(int(input()))

    cnt = [0]*P
    for i in range(P):
        for j in range(N):
            if c[i] in range(ab[j][0], ab[j][1]+1):
                cnt[i] += 1
    print(f'#{t}', end = ' ')
    for k in cnt:
        print(k, end=' ')
    print()
