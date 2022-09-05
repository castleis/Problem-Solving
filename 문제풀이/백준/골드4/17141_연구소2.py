# 0 : 빈칸, 1 : 벽, 2 : 바이러스
from itertools import combinations
import sys
input = sys.stdin.readline

def virus(info):
    viruss = []
    virus_cnt = 0
    for i in range(N):
        for j in range(N):
            if info[i][j] == 2:
                viruss.append((i,j))
                info[i][j] = 0
                virus_cnt += 1
            elif info[i][j] == 0:
                virus_cnt += 1
    return viruss, virus_cnt

def checkk(N,visited):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                return False

def pandemic(virus, info, virus_cnt):
    virus_set = combinations(virus, M)
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    days = []
    for lst in virus_set:
        stack = list(lst[:])
        day= 0
        visited = [[-1]*N for _ in range(N)]
        cnt = virus_cnt
        for x,y in stack:
            visited[x][y] = 0
            cnt -= 1

        while stack:
            x,y = stack.pop(0)
            for dx,dy in d:
                nx = x+dx
                ny = y+dy
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                    if info[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        stack.append((nx,ny))
                        day = max(day, visited[nx][ny])
                        cnt -= 1
                    if info[nx][ny] == 1:
                        visited[nx][ny] = '-'

        if checkk(N,visited) == False:
            if cnt == 0:
                days.append(day)
            else:
                pass
        else:
            days.append(day)

    if len(days) == 0:
        return -1

    return min(days)

N,M = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(N)]
viruss,virus_cnt = virus(info)
ans = pandemic(viruss, info, virus_cnt)
print(ans)

