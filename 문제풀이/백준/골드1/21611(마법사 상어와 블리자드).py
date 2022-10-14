def make_order(x,y):
    snail = [(x,y)]
    snail_d = [(0,-1),(1,0),(0,1),(-1,0)]

    arr = []
    for i in range(1,N):
        arr.extend([i, i])
    arr += [N]
    d = 0
    for i in range(len(arr)):
        for j in range(arr[i]):
            # print(f'============= {arr[i]} = {j} ===============')
            dx,dy = snail_d[d]
            x,y = x+dx, y+dy
            # print(x,y)
            if 0 <= x < N and 0 <= y < N:
                snail.append((x,y))
        d = (d+1) % 4
    return snail

def blizard(x,y,d,s):
    dx,dy = dire[d]
    for i in range(1,s+1):
        # num = mapp[x + i*dx][y + i*dy]
        # balls[num-1] += 1
        mapp[x + i*dx][y + i*dy] = 0
    
    # print(f'after blizard : {mapp}')
    move()
    # print(mapp)
    return

def explosion():
    while True:
        EXPLOSION = 0
        s,e = 1,2
        while e < len(snail):
            # print(f'======== {s},{e} =========')
            cur_x,cur_y = snail[s]
            if mapp[cur_x][cur_y] == 0:
                break
            next_x, next_y = snail[e]
            if mapp[cur_x][cur_y] != mapp[next_x][next_y]:
                explo_cnt = e - s
                if explo_cnt >= 4:
                    # print(f'폭발~~~ {s},{e} : {explo_cnt}개')
                    EXPLOSION += 1
                    explo_num = mapp[cur_x][cur_y]
                    # print(f'폭발한 구슬 숫자 : {explo_num}')
                    balls[explo_num - 1] += explo_cnt
                    for i in range(s,e):
                        r,c = snail[i]
                        mapp[r][c] = 0
                s = e
            e += 1
        if EXPLOSION == 0:
            break
        move()
    # print(f'after explosion : {mapp}')
    # print(balls)
    return

def change():
    new_mapp = [[0]*N for _ in range(N)]
    idx = 1
    group_cnt = 1
    group_num = mapp[snail[1][0]][snail[1][1]]
    for i in range(1,len(snail)-1):
        # print(f'=========== {i} =============')
        if idx >= len(snail):
            return new_mapp
        x,y = snail[i]
        nx,ny = snail[i+1]
        if mapp[x][y] == mapp[nx][ny]:
            group_cnt += 1
        else:
            # print(f'idx : {idx}, {group_cnt}, {group_num}')
            x,y = snail[idx]
            dx,dy = snail[idx+1]
            new_mapp[x][y] = group_cnt
            new_mapp[dx][dy] = group_num
            group_cnt,group_num = 1, mapp[nx][ny]
            idx += 2
    # print(f'after change : {new_mapp}')
    return new_mapp

def move():
    global mapp
    zeros = 0
    for i in range(1,len(snail)):
        r,c = snail[i]
        if mapp[r][c] == 0:
            zeros += 1
        # print(f'============ {i} : [{r},{c}], zeros : {zeros} ============')
        if zeros > 0 and mapp[r][c] > 0:
            nx,ny = snail[i-zeros]
            # print(r,c, nx,ny)
            mapp[nx][ny] = mapp[r][c]
            mapp[r][c] = 0
    return




N,M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
magic = [tuple(map(int,input().split())) for _ in range(M)]
# (X,Y) : 마법사 상어 위치
x = y = N//2
snail = make_order(x,y)
# print(snail)
dire = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)}
balls = [0]*3
# blizard(x,y,2,2)
for d,s in magic:
    blizard(x,y,d,s)
    explosion()
    new_mapp = change()
    mapp = new_mapp
ans = 0
for i in range(len(balls)):
    ans += balls[i]*(i+1)
print(ans)