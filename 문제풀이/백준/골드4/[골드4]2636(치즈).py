from collections import deque

def melting(cheeses):
    visited = [[0]*V for _ in range(H)]
    air = deque()
    air.append((0,0))
    visited[0][0] = 1
    cnt = 0
    while air:
        x,y = air.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < H and 0 <= ny < V and not visited[nx][ny]:
                if cheeses[nx][ny] == 0:
                    visited[nx][ny] = 1
                    air.append((nx,ny))
                elif cheeses[nx][ny] == 1:
                    cheeses[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    cheese.append(cnt)
    return cnt

H,V = map(int,input().split())
cheeses = [list(map(int,input().split())) for _ in range(H)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
cheese = []

time = 0
while True:
    time += 1
    left = melting(cheeses)
    if left == 0:
        break
print(time-1)
print(cheese[-2])

# Clone coding
import sys
from itertools import count

Directions = ((1,0),(-1,0),(0,1),(0,-1))

def solve(R,C,G):
    if R <= 2 or C <= 2:
        return 0,0
    
    visited = [[False]*C for _ in range(R)]
    air_set = set()
    # 사각형 둘레는 치즈가 놓이지 않으므로 모두 방문처리, air_set 에 추가해준다.
    for r in range(R):
        visited[r][0] = True
        visited[r][C-1] = True
        air_set.add((r,0))
        air_set.add((r,C-1))
    for c in range(C):
        visited[0][c] = True
        visited[R-1][c] = True
        air_set.add((0,c))
        air_set.add((R-1,c))


    remain_cheese_count = 0
    # 이 for문은 어떻게 돌아가는 겅미 @@
    for step in count(0):
        print(step, count(0))
        cheese_set = set()
        while air_set:
            pr,pc = air_set.pop()
            for dr,dc in Directions:
                r,c = pr + dr, pc + dc
                # 범위내에 해당하지 않거나 방문했던 곳이면 continue
                if not(0 <= r < R and 0 <= c < C) or visited[r][c]:
                    continue
                if G[r][c] == 0:
                    air_set.add((r,c))
                    visited[r][c] = True
                else:
                    cheese_set.add((r,c))
        # 남은 치즈가 없다면(끝났다면) 현재 step과 직전의 remain_cheese_count를 return
        if not cheese_set:
            return step, remain_cheese_count
        # 해당사항이 없으면 remain_cheese_count를 갱신해줌.
        remain_cheese_count = len(cheese_set)
        # 현재 녹을 치즈들을 녹도록 하고 방문처리, air_set 에 추가
        for r,c in cheese_set:
            G[r][c] = 0
            visited[r][c] = True
            air_set.add((r,c))
    return -1

def main():
    input = sys.stdin.readline
    R,C = [int(x) for x in input().split()]
    G = [[int(x) for x in input().split()] for _ in range(R)]
    res = solve(R,C,G)
    print(res[0])
    print(res[1])

if __name__ == "__main__":
    main()