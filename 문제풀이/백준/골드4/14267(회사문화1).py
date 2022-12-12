import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = list(map(int,input().split()))
info = [tuple(map(int,input().split())) for _ in range(M)]
info.sort()
W = [0]*(N+1)
for j in range(M):
    i,w = info[j]
    W[i] += w
print(W)
for p in range(1,N):
    boss = nums[p]
    print(f'{p}의 보스 : {boss}, {W[boss]}')
    W[p+1] += W[boss]
print(*W[1:])

'''
2 2
-1 1
2 1
2 3
# 0 4

6 6
-1 1 2 3 3 2
2 123
3 123
4 123
5 123
2 123
3 123
# 0 246 492 615 615 246
'''