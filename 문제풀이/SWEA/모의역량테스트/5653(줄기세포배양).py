import sys
sys.stdin = open('input/5653.txt')

for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    cells = []
    active = 0
    # arr 확장해주기 -> 상하좌우 K씩 늘려주기
    for i in range(N):
        arr[i] = [0]*K + arr[i] + [0]*K
    arr = [[0]*(M+2*K) for _ in range(K)] + arr + [[0]*(M+2*K) for _ in range(K)]

    for i in range(N+2*K):
        for j in range(M+2*K):
            if arr[i][j] != 0:
                cells.append((0,i,j,arr[i][j]))
                arr[i][j] = 1004
                active += 1
    # print(f'초기 줄기세포 : {active}')
    alive, dead = [], []
    time = 0
    # while보다 for문이 빠르니까... for time in range(1,K+1): 로 하면 더 빠르지 않을까~
    while time < K:
        for _ in range(len(cells)):
            t,x,y,X = cells.pop(0)
            t += 1
            if t < X:
                cells.append((t,x,y,X))
            # 활성 후 1시간이 지났으므로
            elif t == X:
                alive.append((0,x,y,X))

        # sort 해서 큰 친구부터 분열쓰
        alive.sort(key = lambda x : x[3], reverse = True)
        for _ in range(len(alive)):
            t,x,y,X = alive.pop(0)
            if t == 0:
                alive.append((t+1,x,y,X))
            else:
                for dx,dy in d:
                    nx,ny = x+dx, y+dy
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = X
                        cells.append((0,nx,ny,X))
                        active += 1
                dead.append((1,x,y,X))

        for _ in range(len(dead)):
            t,x,y,X = dead.pop(0)
            # t += 1
            if t < X:
                dead.append((t+1,x,y,X))
            else:
                active -= 1
        time += 1

    print(f'#{tc} {active}')


# 빠른 풀이..!!!!!!!!!!!!!!!!!!!!!!!
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
T = int(input())
 
for tc in range(1, T + 1):
    n, m, k = map(int, input().split()) # n * m사이즈에서 k시간 이후 상태 구하기
    graph = [list(map(int, input().split())) for _ in range(n)]
 

    # - 상하좌우 K만큼 늘렸기 때문에 처음부터 그에 맞는 cell 리스트를 만들어 준 다음
    #   graph를 탐색, 세포가 있다면 cell에 해당하는 위치는 [i+k][j+k] 임!!
    # - 줄기세포의 크기는 1~10 이므로 크기를 인덱스로 하는 cell_life 리스트를 선언, 
    #   해당 크기의 줄기세포를 크기에 맞는 인덱스에 넣어준다
    cell = [[0] * (2 * k + m) for _ in range(2 * k + n)]
    cell_life = [[] for _ in range(11)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                cell[i + k][j + k] = graph[i][j]
                cell_life[graph[i][j]].append((i + k, j + k))
    
    # 총 k 시간동안 분열 시작
    for time in range(1, k + 1):
        # 크기가 큰 친구부터 분열 시작
        for idx in range(10, 0, -1):
            # 흐른 시간(time)과 세포 크기(idx+1)가 같을 때 세포가 활성
            if time % (idx + 1) != 0:
                continue
            temp = []
            for x, y in cell_life[idx]:
                # 분열 시 세포 크기보다 남아 있는 시간이 크면 세포가 사라지므로
                # 남아 있는 시간이 작을 때만 다시 넣어주기 위해 temp에 append
                if (k - time) < idx - 1:
                    temp.append((x, y))
                # 상하좌우로 세포 분열
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if cell[nx][ny] == 0:
                        cell[nx][ny] = idx
                        # 새로운 세포를 temp에 넣어줌 
                        temp.append((nx, ny))
            # 현재 세포 크기 위치에 temp로 대체
            cell_life[idx] = temp
 
    result = 0
    # 남아있는 세포의 갯수를 count
    for i in range(11):
        result += len(cell_life[i])
    print("#%d %d" %(tc, result))