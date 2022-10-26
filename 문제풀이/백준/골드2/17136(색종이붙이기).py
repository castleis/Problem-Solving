def change(x,y,k,n):
    global mapp, papers
    for i in range(x,x+k):
        for j in range(y, y+k):
            mapp[i][j] = n
    if n == 1:
        papers[k] += 1
        # print(f'change1 [{x},{y}] {k} : {papers[k]}')
    elif n == 0:
        papers[k] -= 1
        # print(f'change0 [{x},{y}] {k} : {papers[k]}')

def cando(x,y,k):
    if x+k > 10 or y+k > 10:
        return False
    # print(f'===={x},{y}=====')
    for i in range(x,x+k):
        for j in range(y,y+k):
            if not mapp[i][j]:
                # print(f'cantdo : {i},{j}')
                return False
    return True

def solve(idx,inter_cnt):
    global minn, papers
    if inter_cnt > minn:
        return
    if idx >= 100:
        minn = inter_cnt
        return
    i = idx // 10
    j = idx % 10
    if mapp[i][j]:
        for k in range(5,0,-1):
            if cando(i,j,k) and papers[k]:
                change(i,j,k,0)
                solve(idx+k, inter_cnt+1)
                change(i,j,k,1)
    else:
        solve(idx+1, inter_cnt)
    
mapp = [list(map(int,input().split())) for _ in range(10)]
minn = 1000000000
papers = [5]*6
solve(0,0)
if minn == 1000000000:
    minn = -1
print(minn)
