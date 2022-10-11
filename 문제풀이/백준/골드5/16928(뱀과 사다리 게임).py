N,M = map(int,input().split())
ladder = {}
snake =  {}
for _ in range(N):
    x,y = map(int,input().split())
    ladder[x] = y
for _ in range(M):
    x,y = map(int,input().split())
    snake[x] = y

def solve():
    queue = [(1,0)]
    visited = [0]*101

    while queue:
        # C는 현재 주사위 굴린 횟수
        S,C = queue.pop(0)
        if S == 100:
            return C
        for i in range(1,7):
            new = S+i
            if new <= 100 and not visited[new]:
                # 사다리나 뱀이 있다면 새로운 위치 new를 사다리와 뱀을 타고 난 뒤의 위치로 바꿔준다
                if new in ladder.keys():
                    new = ladder[new]
                elif new in snake.keys():
                    new = snake[new]
                # 도착할 장소가 아직 방문하지 않았다면 go, 아니면 pass
                if not visited[new]:
                    queue.append((new,C+1))
                    visited[new] = 1
# print()
print(solve())
