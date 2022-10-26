def fish_move():
    global mapp, fishes
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
        # print(f'{f} 물고기 {d}이동 후: {mapp}')

def shark_move(shark, cnt):
    global mapp
    while True:
        print(f'===================== {shark} ========================')
        fish_move()
        print(mapp)
        i,j,d = shark
        di, dj = dire[d]
        n = 1
        eating = []
        while 0 <= i+n*di < 4 and 0 <= j+n*dj < 4:
            ni,nj = i+n*di, j+n*dj
            if mapp[ni][nj]:
                f = mapp[ni][nj]
                eating.append((f,ni,nj,fishes[f][2]))
                # 물고기를 만나면 (번호, 방향) 순으로 eating 리스트에 넣어주기
            n += 1

        if eating:
            eating.sort()
            print(f'먹이 후보 : {eating}')
            C = False
            for m in range(len(eating)-1,-1,-1):
                f,x,y,d = eating[m]
                dx,dy = dire[d]
                if 0 <= x+dx < 4 and 0 <= y+dy < 4:
                    print(f'먹는당 : {f}')
                    cnt += f
                    mapp[i][j],mapp[x][y] = 0,1004
                    shark = (x,y,fishes[f][2])
                    fishes.pop(f)
                    print(f'after - shark : {shark}')
                    print(f'interval-cnt : {cnt}')
                    print(mapp)
                    C = True
                    break
            if C:
                continue
            else:
                f,x,y,d = eating.pop()
                print(f'끝끝, {f}')
                cnt += f
        return cnt
                

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
fish, mapp[0][0] = mapp[0][0], 1004
d = fishes[fish][2]
fishes.pop(fish)
shark = (0,0,d)
# print(f'shark in : {shark}, {mapp}')
ans = shark_move(shark,fish)
print(ans)