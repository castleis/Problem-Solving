from copy import deepcopy
def fish_move(sea):
    global fishes
    mapp = deepcopy(sea)
    # fishes = deepcopy(mulgogi)
    # print(f'??????????????? : {list(fishes.keys())}')
    # print(f'???????????? {mapp}')

    for f in sorted(fishes.keys()):
        i,j,d = fishes[f]
        # print(f'========== {f} 번 물고기 {d} 방향 이동 ============')
        # print(fishes[f])
        di,dj = dire[d]
        ni,nj = i+di, j+dj
        # 가야할 곳이 범위 밖이거나, 상어가 있는 경우 -> 여기서 걸러야할거 다 거르고 d만 바꿔서 한번에 옮겨주는걸로
        if ni < 0 or ni >3 or nj < 0 or nj > 3 or mapp[ni][nj] == 1004:
            while True:
                # print(f'빙글빙글~~~~~~~~~~~~~~')
                # 반시계로 45도 돌아주기
                d = (d + 1) % 8
                di,dj = dire[d]
                ni,nj = i+di, j+dj
                # 범위 안에 들어오고 상어 자리가 아니라면
                if 0 <= ni < 4 and 0 <= nj < 4:
                    if mapp[ni][nj] != 1004:
                        # 다른 물고기가 있다면 자리 바꿔주기
                        # print(mapp[ni][nj], mapp[i][j])
                        of = mapp[ni][nj]
                        if of != 0:
                            fishes[of] = (i,j,fishes[of][2])
                        fishes[f] = (ni,nj,d)
                        mapp[i][j], mapp[ni][nj] = mapp[ni][nj],mapp[i][j]
                        break
        # 범위 내로 옮기는 경우
        else:
            # print(mapp[ni][nj], mapp[i][j])
            of = mapp[ni][nj]
            # print(fishes[f])
            # print(f'옮길 사람 : {of}')
            if of != 0:
                fishes[of] = (i,j,fishes[of][2])
            fishes[f] = (ni,nj,d)
            mapp[i][j], mapp[ni][nj] = mapp[ni][nj], mapp[i][j]
        # print(f'{f} 물고기 {d}로 이동 후: {mapp}')
    # print(f'이동 끝난 후 fishes : {fishes}')
    return mapp

def shark_move(shark, cnt, sea):
    global result, fishes
    while True:
        # print(f'===================== {shark} ========================')
        # 맵과 물고기 프로필을 딥카피해서 물고기 옮겨주기
        mapp = fish_move(sea)
        # print(f'after fish move : {mapp}')
        # print(fishes)
        # 상어의 정보
        i,j,d = shark
        di, dj = dire[d]
        n = 1
        # 범위 내를 쭉 가면서 물고기가 있다면 포획하기
        while 0 <= i+n*di < 4 and 0 <= j+n*dj < 4:
            ni,nj = i+n*di, j+n*dj
            # 물고기를 만나면 (번호, 방향) 순으로 eating 리스트에 넣어주기
            if mapp[ni][nj]:
                f = mapp[ni][nj]
                f,x,y,d = f,ni,nj,fishes[f][2]
                # print(f'====== {f}먹을 차례, {cnt} =======')
                # print(mapp)
                cnt += f
                # 상어와 자리를 바꿔주고 머금, 상어 스펙 바꿔주기
                mapp[i][j],mapp[x][y] = 0,1004
                # print(f'되돌려놓기 {mapp[i][j]}')
                # print(f'after eating- mapp : {mapp}')
                shark = (x,y,fishes[f][2])
                # 먹힌 친구는 물고기 딕셔너리에서 pop
                fishes.pop(f)
                # print(f'interval-cnt : {cnt}')
                # 현재까지 먹은 상태의 맵과 물고기 딕셔너리를 다음 재귀로 넘겨주기
                # print(f'넘겨줄 fishes: {fishes}')
                shark_move(shark,cnt,mapp)
                # 재귀에서 돌아나오면 다시 물고기 리스트에 넣어주기... 물고기 부활~!!~!~~!
                fishes[f] = (x,y,d)
                mapp[x][y],mapp[i][j] = f,1004
                cnt -= f
            n += 1
                # print(f'복구 되었니? {fishes}')
                # print(f'mapp 복구 되었니? {mapp}')
        # 먹이 리스트가 텅텅ㅇ 비었다면~
        # print(f'먹을게 없당')
        # result와 비교해서 더 많이 먹었다면 최댓값 갱신해주고 return
        if cnt > result:
            result = cnt
            # mapp = sea
            # print(f'최대값 갱신 : {result}')
        return
                

dire = {0:(-1,0), 1:(-1,-1), 2:(0,-1), 3:(1,-1), 4:(1,0), 5:(1,1), 6:(0,1), 7:(-1,1)}

# 물고기 번호를 키로하는 방향 딕셔너리, 물고기의 위치 맵
fishes, sea = {}, []
for i in range(4):
    arr = list(map(int,input().split()))
    map_arr = []
    for j in range(4):
        fishes[arr[2*j]] = (i,j,arr[2*j+1]-1)
        map_arr.append(arr[2*j])
    sea.append(map_arr)
# print(fishes)
fish, sea[0][0] = sea[0][0], 1004
d = fishes[fish][2]
fishes.pop(fish)
shark = (0,0,d)
result = 0
# print(f'shark in : {shark}, {sea}')
shark_move(shark,fish,sea)
print(f'final result : {result}')