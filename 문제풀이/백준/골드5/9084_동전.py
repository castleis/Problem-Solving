import sys
sys.setrecursionlimit(10**5)
def dp(x):
    if x >= goal:
        return 
    print('=============', x)
    for coin in coins:
        cnts[x] += cnts[coin]
    print(cnts[x])
    for coin in coins:
        dp(x+coin)

T = int(input())
for t in range(1):
    N = int(input())
    coins = list(map(int,input().split()))
    goal = int(input())
    cnts = [0]*(10**9)
    for coin in coins:
        cnts[coin] = 1
    dp(sum(coins))
    print(cnts[goal])