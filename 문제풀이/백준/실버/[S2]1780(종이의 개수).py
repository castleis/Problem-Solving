def solve(x,y,k):
    global ans
    # print(f'=================={k}=======================')
    if k == 0:
        return
    n = mapp[x][y]
    check = [n]*k
    # print(f'check : {check}')
    tears = False
    for i in range(k):
        if mapp[x+i][y:y+k] != check:
            tears = True
            break
    if tears:
        m = k//3
        for i in range(3):
            for j in range(3):
                # print(f'여기로 재귀 : {x+m*i},{y+m*j}, m : {m}')
                solve(x+m*i, y+m*j, m)
    else:
        # print(f'success!!! : [{x},{y}], {k}')
        ans[n+1] += 1
        # print(ans)
        return

N = int(input())
mapp = [list(map(int,input().split())) for _ in range(N)]
ans = [0]*3
solve(0,0,N)
for i in ans:
    print(i)

# for i in range(3):
#     for j in range(3):
#         print(i,j)