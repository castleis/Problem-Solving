from collections import deque
import sys
input = sys.stdin.readline

def solve(a):
    V = [0]*(N+1)
    Q = deque([a])
    V[a] = 1
    while Q:
        A = Q.popleft()
        for city in ways[A]:
            if not V[city]:
                V[city] = V[A] + 1
                Q.append(city)
    V = [0] + [v-1 for v in V[1:]]
    return V

N,M = map(int,input().split())
ways = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    ways[A].append(B)
    ways[B].append(A)

spent_time = [[]]
for a in range(1,N+1):
    spent_time.append(solve(a))

min_time = sys.maxsize
chicken_house = (0,0)
for a in range(1,N+1):
    for b in range(a+1,N+1):
        if a == b:
            continue
        summ = sum(min(spent_time[a][k], spent_time[b][k]) for k in range(1,N+1))
        if min_time > summ:
            min_time = summ
            chicken_house = (a,b)
print(*chicken_house, min_time*2)