from collections import deque
def move_to_conv(queue):
    new_queue = deque()
    while queue:
        i,j,n = queue.popleft()
        # print(f'================ [{i},{j}] =================')
        if is_arrived[n]:   # 이미 편의점에 도착한 사람 번호라면 continue
            continue
        for di, dj in directions:
            ni, nj = i+di, j+dj
            # print(f'====== [{ni},{nj}] =======')
            if 0 <= ni < gird_size and 0 <= nj < gird_size and not visited[ni][nj][n]:
                if mapp[ni][nj] == -1:
                    continue
                if mapp[ni][nj] == n+1:
                    mapp[ni][nj] = -1 # 더이상 지나갈 수 없음
                    is_arrived[n] = 1
                new_queue.append((ni,nj,n))
                visited[ni][nj][n] = 1
                # print('visited :' ,visited[ni], visited[ni][nj])
    # print('after move_to_conv : ',mapp)
    return new_queue

def move_to_basecamp(t):
    des_i, des_j = destination[t]
    # print(f'{t+1}번 사람이 가려는 편의점 : [{des_i},{des_j}]')
    queue = deque([(des_i,des_j)])
    basecamp_visited = [[0]*gird_size for _ in range(gird_size)]
    candidate_basecamp = []
    stop = False
    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()
            for di, dj in directions:
                ni,nj = i+di, j+dj
                if 0 <= ni < gird_size and 0 <= nj < gird_size and not basecamp_visited[ni][nj]:
                    if mapp[ni][nj] == 1:
                        candidate_basecamp.append((ni,nj))
                        stop = True
                    if mapp[ni][nj] == -1:
                        continue
                    queue.append((ni,nj))
                    basecamp_visited[ni][nj] = 1
        if stop:
            candidate_basecamp.sort()
            base_i, base_j = candidate_basecamp[0]
            mapp[base_i][base_j] = -1
            # print(f'베이스캠프 좌표 : [{base_i, base_j}]')
            # print(f'after move_to_basc : ', mapp)
            return base_i, base_j

gird_size, person_num = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(gird_size)]
destination = []
for num in range(1,person_num+1):
    x,y = map(int,input().split())
    destination.append((x-1, y-1))
    mapp[x-1][y-1] = num+1
directions = [(-1,0),(0,-1),(0,1),(1,0)]
visited = [[[0]*(person_num+1) for _ in range(gird_size)] for _ in range(gird_size)]
is_arrived = [0]*(person_num+1)
time = 0
queue = deque()
while sum(is_arrived) < person_num:
# while time < 22:
    # print(f'========================= {time} =================================')
    queue = move_to_conv(queue)
    if time < person_num:
        base_i, base_j = move_to_basecamp(time)
        queue.append((base_i, base_j, time+1))
    time += 1
    # print('is_arrived : ',is_arrived)
print(time)
'''
11 21
0 0 1 0 0 1 1 1 0 0 1
1 1 1 1 1 1 1 0 0 1 1
0 0 0 0 1 0 1 0 1 0 1
1 0 0 0 0 0 0 1 1 1 1
0 1 0 1 1 0 1 1 0 0 1
0 1 0 1 0 1 0 1 0 0 1
0 0 0 1 0 0 1 1 1 1 0
1 1 1 1 0 0 0 1 0 1 0
1 1 1 1 0 1 1 1 1 1 1
1 1 0 0 0 1 1 1 0 0 1
1 1 0 1 1 0 0 1 1 0 1
10 10
5 9
11 10
7 3
4 4
11 6
1 2
5 3
3 8
2 8
3 3
9 5
1 1
3 4
7 11
8 11
1 9
6 10
11 3
3 2
6 1
'''