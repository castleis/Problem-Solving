import sys
input = sys.stdin.readline
from collections import deque

def find(box):
    tomato_num = 0
    ripped = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                ripped.append((i,j))
            elif box[i][j] == 0:
                tomato_num += 1
    return ripped, tomato_num

def isRipe(box,N, M):
    ripped,tomato_num = find(box)
    if tomato_num == 0:
        return 0
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    day = 0
    while ripped:
        day += 1
        for _ in range(len(ripped)):
            x,y = ripped.popleft()
            for dx, dy in d:
                nx = x+dx
                ny = y+dy
                if 0 <= nx < N and 0 <= ny < M and not box[nx][ny]:
                    box[nx][ny] = day
                    ripped.append((nx,ny))
                    tomato_num -= 1
    if tomato_num == 0:
        return day-1
    else:
        return -1

# M : 가로, N : 세로
M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
print(isRipe(box,N, M))