from collections import deque
import sys
input = sys.stdin.readline
preset = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
          'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
          'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
def bfs(a):
    V = [0]*N
    Q = deque([a])
    V[a] = 1
    while Q:
        x = Q.popleft()
        for y in parent[x]:
            if not V[y]:
                if y in knowns:
                    continue
                # 부모를 타고 올라가다가 마약 공급원을 만나면 True를 리턴
                if y in root:
                    return True
                Q.append(y)
                V[y] = 1
    # 마약 공급원을 만나지 못하면 False를 리턴
    return False

N,M = map(int,input().split())
parent = [[] for _ in range(N)]
for _ in range(M):
    x,y = input().split()
    a,b = preset[x], preset[y]
    parent[b].append(a)
    print(parent)
num, *info = input().split()
knowns = set()
for n in info:
    knowns.add(preset[n])
root = set()
for i in range(N):
    # print(parent[i])
    if not parent[i]:
        root.add(i)
print(root)
ans = 0
check = set(i for i in range(N)) - root - set(knowns)
for a in check:
    # print(f'======={a}')
    if bfs(a):
        ans += 1
print(ans)