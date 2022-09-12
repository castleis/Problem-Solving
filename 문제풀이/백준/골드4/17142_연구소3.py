from itertools import combinations
import sys
input = sys.stdin.readline
'''
!!반례 테스트케이스!!
9 1
0 2 2 2 2 2 2 2 0
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
# 4
'''

def findvirus(info):
    viruss = []
    virus_cnt = 0
    for i in range(N):
        for j in range(N):
            if info[i][j] == 2:
                viruss.append((i,j))
                info[i][j] = '*'
            elif info[i][j] == 0:
                virus_cnt += 1
    return viruss, virus_cnt

def makevirus(virus, info, virus_cnt):
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
                    elif info[nx][ny] == '*':
                        if cnt > 0:
                            visited[nx][ny] = visited[x][y] + 1
                            stack.append((nx,ny))
        if cnt == 0:
            days.append(day)
    if len(days) == 0:
        return -1
    return min(days)

N,M = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(N)]
viruss,virus_cnt = findvirus(info)
print(makevirus(viruss, info, virus_cnt))

