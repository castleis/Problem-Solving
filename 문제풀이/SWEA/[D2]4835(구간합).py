T = int(input())
for t in range(1, T+1):
    N,M = input().split()
    v = list(map(int, input().split()))
    n,m = int(N), int(M)
    sums = []
    for i in range(n-m+1):
        sub = 0
        for j in range(m):
            sub += v[i+j]
        sums.append(sub)
    result = max(sums)-min(sums)
    print(f'#{t} {result}')

