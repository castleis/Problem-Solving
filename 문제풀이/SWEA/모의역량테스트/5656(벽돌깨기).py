import sys
sys.stdin = open('input/5656.txt')

from collections import deque
# 구슬을 떨어뜨린 횟수와 위치에 대한 탐색은 DFS, 떨어뜨리고 난 후 연쇄작용은 BFS로
# h(x) : 가로, w(y) : 세로
def map_making(arrs):
    mapp = [[0]*W for _ in range(H)]
    for w in range(W):
        for h in range(H):
            mapp[h][w] = arrs[h][w]
    return mapp

def crush(w,cur_h,mapp):
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    queue = deque()
    queue.append((cur_h,w,mapp[cur_h][w]))
    mapp[cur_h][w] = 0
    crushed = 1
    while queue:
        # print(queue)
        x,y,p = queue.popleft()
        for dx, dy in d:
            for n in range(1,p):
                nx,ny = x+n*dx, y+n*dy
                if 0 <= nx < H and 0 <= ny < W and mapp[nx][ny] != 0:
                    if mapp[nx][ny] != 1:
                        queue.append((nx,ny,mapp[nx][ny]))
                    crushed += 1
                    mapp[nx][ny] = 0
    # print()
    # print(f'after crushed : {mapp}')
    # print(f'crushed : {crushed}')
    return crushed

def sortt(mapp):
    for w in range(W):
        zeros = 0
        for h in range(H-1,-1,-1):
            if mapp[h][w] == 0:
                zeros += 1
            else:
                if zeros > 0:
                    mapp[h+zeros][w] = mapp[h][w]
                    mapp[h][w] = 0
    return mapp

def dfs(crushed,k,arrs):
    global maxx
    if crushed == bricks:
        maxx = crushed
        return
    if k == N:
        if maxx < crushed:
            maxx = crushed
            # print(maxx)
        return
    for w in range(W):
        mapp = map_making(arrs)
        cur_h = -1
        for h in range(H):
            if mapp[h][w] == 0:
                pass
            else:
                cur_h = h
                break
        if cur_h != -1:
            result = crush(w,cur_h,mapp)
            mapp = sortt(mapp)
            # print(f'after sorted : {mapp}')
            dfs(crushed+result,k+1,mapp)
    

for t in range(1,int(input())+1):
    N,W,H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    bricks = 0
    for i in range(W):
        for j in range(H):
            if arr[j][i] != 0:
                bricks += 1
    maxx = 0
    dfs(0,0,arr)
    ans = bricks - maxx
    # print(bricks,maxx)
    print(f'#{t} {ans}')