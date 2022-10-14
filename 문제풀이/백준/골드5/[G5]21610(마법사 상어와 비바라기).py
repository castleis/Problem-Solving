# 백준 21610 마법사 상어와 비바라기
from collections import deque
dire = {1 : (0,-1), 2 : (-1,-1), 3 : (-1,0), 4 : (-1,1), 5 : (0,1), 6 : (1,1), 7 : (1,0), 8 : (1,-1)}
diag = [(1,1),(1,-1),(-1,1),(-1,-1)]

def rainy():
    for d,s in move:
        dx,dy = dire[d]
        after_move = deque()
        rained = [[0]*N for _ in range(N)]
        # print(f'========== {d} : [{dx},{dy}] ,{s} ============')
        # 구름을 모두 다 이동시키고 난 후 비를 뿌리기 때문에 이동 후의 좌표를 다시 넣어주기
        for _ in range(len(cloud)):
            i,j = cloud.pop(0)
            i = (i + s*dx) % N
            j = (j + s*dy) % N
            after_move.append((i,j))
            arr[i][j] += 1
            rained[i][j] = 1
        # print(after_move)

        for _ in range(len(after_move)):
            i,j = after_move.popleft()
            # 비 내리고, 비 내린 곳 체크
            # 물 복사
            adj_cnt = 0
            for di,dj in diag:
                ni,nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                    # print((i,j),(ni,nj))
                    adj_cnt += 1
            arr[i][j] += adj_cnt
        
        for i in range(N):
            for j in range(N):
                # 물의 양이 2 이상이고, 직전에 비가 내리지 않은 곳이면 cloud에 추가, 2를 빼줌
                if arr[i][j] >= 2 and not rained[i][j]:
                    cloud.append((i,j))
                    arr[i][j] -= 2
        # print(arr,cloud)
    
    sums = 0
    for i in range(N):
        for j in range(N):
            sums += arr[i][j]
    return sums

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
move = [tuple(map(int,input().split())) for _ in range(M)]
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
print(rainy())
