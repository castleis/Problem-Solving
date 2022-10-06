from collections import deque

N,M = map(int,input().split())
ladder = [tuple(map(int,input().split())) for _ in range(N)]
snake = [tuple(map(int,input().split())) for _ in range(M)]
LS,LE = sorted(ladder,key = lambda x : (x[1]-x[0]), reverse = True)[0]
snake.sort()

queue = deque()
queue.append(1)
visited = [0]*101
while queue:
    S = queue.popleft()