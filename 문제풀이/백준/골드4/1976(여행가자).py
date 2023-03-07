'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    queue.append(start)
    V = [0]*(N+1)
    # print('V :',V)
    V[start] = 1
    while queue:
        city = queue.popleft()
        for dc in range(1,N+1):
            # print(f'=============== {dc}')
            # print(maps[city][dc-1])
            if maps[city][dc-1] and not V[dc]:
                # print(f'====== 연결된 도시 번호 : {dc}')
                if dc == end:
                    # print('V :',V)
                    return True
                queue.append(dc)
                V[dc] = 1
    return False

def solve():
    if M == 1:
        return 'YES'
    for i in range(M-1):
        start, end = schedule[i], schedule[i+1]
        if start == end:
            continue
        print(f'=============[{start},{end}]===============')
        if bfs(start, end):
            continue
        else:
            return 'NO'
    return 'YES'

N = int(input())
M = int(input())
maps = [[] for _ in range(N+1)]
for i in range(1,N+1):
    maps[i] += list(map(int,input().split()))
    # for j in range(N):
    #     if info[j]:
    #         maps[i].append(j+1)
schedule = list(map(int,input().split()))
print(maps)
# print(schedule)
print(solve())
'''

'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    queue.append(start)
    V = [0]*(N+1)
    V[start] = 1
    while queue:
        city = queue.popleft()
        for next in maps[city]:
            if not V[next]:
                if next == end:
                    return True
                queue.append(next)
                V[next] = 1
    return False

def solve():
    if M == 1:
        return 'YES'
    for i in range(M-1):
        start, end = schedule[i], schedule[i+1]
        if start == end:
            continue
        if bfs(start, end):
            continue
        else:
            return 'NO'
    return 'YES'

N = int(input())
M = int(input())
maps = [[] for _ in range(N+1)]
for i in range(1,N+1):
    info = list(map(int,input().split()))
    for j in range(N):
        if info[j]:
            maps[i].append(j+1)
schedule = list(map(int,input().split()))
print(solve())
'''

# Find - Union 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
root = [n for n in range(N)]

def find(x):
    while x != root[x]:
        x = root[x]
    return x

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        root[root_x] = root[root_y] = min(root_x, root_y)
    return

for i in range(N):
    info = list(map(int,input().split()))
    for j in range(N):
        if info[j]:
            union(i,j)

schedule = list(map(lambda x: int(x)-1,input().split()))
# print('schedule : ', schedule)
def solve():
    for city in range(M-1):
        start, end = schedule[city], schedule[city+1]
        # print(start, end)
        if find(start) != find(end):
            return 'NO'
    return 'YES'
print(solve())

# def is_union(a,roots):
#     que = [a]
#     V = [0]*(N+1)
#     V[root[a]] = 1
#     while que:
#         city = que.pop()
#         if root[city] == roots:
#             return True
#         elif root[city] != roots and not V[root[city]]:
#             que.append(root[city])
#             V[root[city]] = 1
#     return False
