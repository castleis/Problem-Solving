# def dfs(i,j,money, visited):
#     global min_money
#     if money > min_money:
#         return
#     if i == j == N-1:
#         if money < min_money:
#             min_money = money
#         return
#     for di, dj in D:
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             dfs(ni,nj, money + cave[ni][nj], visited)
#             visited[ni][nj] = 0
import heapq
def dijkstra_heap(N):
    heap = [(cave[0][0], 0, 0)]
    while heap:
        money, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            return money
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and cave[nx][ny] != -1:
                heapq.heappush(heap, (money + cave[nx][ny], nx, ny))
                cave[nx][ny] = -1
                
import sys
from collections import deque
input = sys.stdin.readline
def in_range(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def dijkstra(i,j):
    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        cur_cost = cost[x][y]
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            if in_range(nx,ny) and cur_cost + cave[nx][ny] < cost[nx][ny]:
                cost[nx][ny] = cur_cost + cave[nx][ny]
                queue.append((nx,ny))    
    return

t = 1
while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(N)]
    cost = [[1e9]*N for _ in range(N)]
    cost[0][0] = cave[0][0]
    D = [(1,0),(0,1),(-1,0),(0,-1)]
    # dijkstra(0,0)
    # print(f'Problem {t}:', cost[N-1][N-1])
    total_cost = dijkstra_heap(N)
    print(f'Problem {t}:', total_cost)
    t += 1

'''
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0
'''