def solve(x,y,n):
    global B,W
    if n == 0:
        return
    num = mapp[x][y]
    # print(f'================= {n} ==================')
    # print(f'======= num : {num} / [{x},{y}]=========')
    recur = False
    if mapp[x+n-1][y+n-1] == num:
        check = [num]*n
        for i in range(n):
            if mapp[x+i][y:y+n] != check:
                # print(f'{x+i},{y+j} => {mapp[x+i][y+j]}')
                recur = True
                n //= 2
                break
        if not recur:
            if num == 1:
                B += 1
            else:
                W += 1
            # print(f'W:{W}, B:{B}')
    else:
        recur = True
        n //= 2
    # print(f'recur : {recur}')
    if recur:
        for i in range(2):
            for j in range(2):
                solve(x+n*i, y+n*j, n)

N = int(input())
mapp = [list(map(int,input().split())) for _ in range(N)]
B,W = 0,0
solve(0,0,N)
print(W)
print(B)