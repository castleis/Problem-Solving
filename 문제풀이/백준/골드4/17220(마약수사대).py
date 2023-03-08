from collections import deque
import sys
input = sys.stdin.readline
preset = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
          'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
          'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
def bfs(a):
    visited = [0]*N
    Q = deque([a])
    visited[a] = 1
    while Q:
        x = Q.popleft()
        for y in parent[x]:
            if not visited[y] and not V[y]:
                # 부모를 타고 올라가다가 마약 공급원을 만나면 True를 리턴
                if root[y] == 1:
                    return True
                Q.append(y)
                visited[y] = 1
    # 마약 공급원을 만나지 못하면 False를 리턴
    return False

N,M = map(int,input().split())
parent = [[] for _ in range(N)]
root = [1]*N
V = [0]*N
for _ in range(M):
    x,y = input().split()
    a,b = ord(x) - 65, ord(y) - 65
    parent[b].append(a)
    root[b] = 0
num, *info = input().split()
for i in info:
    V[ord(i) - 65] = 1

ans = 0
for a in range(N):
    if V[a] == 1 or root[a] == 1:
        continue
    if bfs(a):
        ans += 1
print(ans)