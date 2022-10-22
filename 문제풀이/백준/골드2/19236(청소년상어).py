from copy import deepcopy
def fish_move(mapp,fishes):
    print(sorted(fishes.keys()))
    for f in sorted(fishes.keys()):
        # print(f'========== {f} 번 물고기 이동 ============')
        i,j,d = fishes[f]
        di,dj = dire[d]
        ni,nj = i+di, j+dj
        if ni < 0 or ni >3 or nj < 0 or nj > 3 or mapp[ni][nj] == 1004:
            while True:
                d = (d + 1) % 8
                di,dj = dire[d]
                ni,nj = i+di, j+dj
                if 0 <= ni < 4 and 0 <= nj < 4:
                    if mapp[ni][nj] != 1004:
                        if mapp[ni][nj]:
                            of = mapp[ni][nj]
                            fishes[of] = (i,j,fishes[of][2])
                            fishes[f] = (ni,nj,d)
                            mapp[i][j], mapp[ni][nj] = of,f
                        elif not mapp[ni][nj]:
                            fishes[f] = (ni,nj,d)
                            mapp[i][j], mapp[ni][nj] = 0, mapp[i][j]
                        break
        elif 0 <= ni < 4 and 0 <= nj < 4:
            if mapp[ni][nj] and mapp[ni][nj] != 1004:
                of = mapp[ni][nj]
                fishes[of] = (i,j,fishes[of][2])
                fishes[f] = (ni,nj,d)
                mapp[i][j], mapp[ni][nj] = of,f
            elif not mapp[ni][nj]:
                fishes[f] = (ni,nj,d)
                mapp[i][j], mapp[ni][nj] = 0, mapp[i][j]
        # print(f'{f} 물고기 이동 후: {mapp}')
    return mapp

def shark_move(shark, info, cnt):
    global maxx
    print(f'===================== {shark} ========================')
    print(f'info : {info}')
    mapp = deepcopy(info)
    mapp = fish_move(mapp, fishes)
    print(f'after fish_move : {mapp}')
    print(info)
    # print(fishes)
    i,j,d = shark
    di, dj = dire[d]
    n = 1
    while 0 <= i+n*di < 4 and 0 <= j+n*dj < 4:
        ni,nj = i+n*di, j+n*dj
        if mapp[ni][nj]:
            f = mapp[ni][nj]
            # 물고기를 만나면 (번호, 방향) 순으로 eating 리스트에 넣어주기
            print(f'먹는당 : {f}')
            cnt += f
            mapp[i][j],mapp[ni][nj] = 0,1004
            shark = (ni,nj,fishes[f][2])
            fishes.pop(f)
            next = deepcopy(mapp)
            print(f'after - shark, cnt : {shark}, {cnt}')
            print(f'재귀 전 맵 : {next}')
            shark_move(shark, next, cnt)
        n += 1
    if maxx < cnt:
        maxx = cnt
    print(f'interval-maxx : {maxx}')
    print(f'return : {info}')
    print()
    # print(f'after - shark, cnt : {shark}, {cnt}')
    # print(mapp)
    return

dire = {0:(-1,0), 1:(-1,-1), 2:(0,-1), 3:(1,-1), 4:(1,0), 5:(1,1), 6:(0,1), 7:(-1,1)}

# 물고기 번호를 키로하는 방향 딕셔너리, 물고기의 위치 맵
fishes, mapp = {}, []
for i in range(4):
    arr = list(map(int,input().split()))
    map_arr = []
    for j in range(4):
        fishes[arr[2*j]] = (i,j,arr[2*j+1]-1)
        map_arr.append(arr[2*j])
    mapp.append(map_arr)
maxx = 0
fish, mapp[0][0] = mapp[0][0], 1004
d = fishes[fish][2]
fishes.pop(fish)
shark = (0,0,d)
# print(f'shark in : {shark}, {mapp}')
shark_move(shark, mapp, 0)
print(f'main-maxx : {maxx}')
print(maxx)