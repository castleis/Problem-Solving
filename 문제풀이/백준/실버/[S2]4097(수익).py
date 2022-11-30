import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:
        quit()
    DP = [0]*(N+1)
    ans = -sys.maxsize
    for i in range(1,N+1):
        num = int(input())
        DP[i] = max(DP[i-1]+num, num)
        if DP[i] > ans:
            ans = DP[i]
    print(ans)
    # print(f'P : {P}')
    # Fenwick = [0] * (N+1)
    # for i in range(1,N+1):
    #     value = P[i]
    #     while i <= N+1:
    #         Fenwick[i] += value
    #         i += (i & -i)
    # print(f'Fenwick : {Fenwick}')
