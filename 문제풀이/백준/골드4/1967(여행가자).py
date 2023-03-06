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