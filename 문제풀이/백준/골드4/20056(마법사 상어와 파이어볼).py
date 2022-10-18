from collections import defaultdict
dire = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}

def move():
    mapp = defaultdict(list)
    for _ in range(len(fireballs)):
        r,c,m,s,d = fireballs.pop()
        dr,dc = dire[d]
        nr,nc = (r+s*dr)%N, (c+s*dc)%N
        mapp[(nr,nc)].append((m,s,d))
    # print(f'mapp : {mapp}, fireballs : {fireballs}')
    return fireball(mapp,fireballs)

def fireball(mapp,fireballs):
    '''
    for (x,y), vals in mapp.items():
        if len(vals) == 1:
            fireballs.append((x,y,*vals[0]))
            continue
        nm,ns,nd = 0,0,[]
        for m,s,d in vals:
            nm += m
            ns += s
            nd.append(d%2)
        nm //= 5
        ns /= len(vals)
        nd = (0,2,4,6) if all(d == nd[0] for d in nd) else (1,3,5,7)
        if nm != 0:
            for d in nd:
                fireballs.append((x,y,nm,ns,d))
    '''
    for i,j in mapp.keys():
        if len(mapp[(i,j)]) > 1:
            Num,M,S = len(mapp[(i,j)]),0,0
            D = []
            for m,s,d in mapp[(i,j)]:
                M += m
                S += s
                D.append(d%2)
            new_m = M//5
            if new_m == 0:
                continue
            new_s = S//Num
            if D.count(1) == Num or D.count(0) == Num:
                new_d = [0,2,4,6]
            else:
                new_d = [1,3,5,7]

            for nd in new_d:
                fireballs.append((i,j,new_m,new_s,nd))
        else:
            m,s,d = mapp[(i,j)][0]
            fireballs.append((i,j,m,s,d))
    return fireballs

N,M,K = map(int,input().split())
fireballs = [list(map(int,input().split())) for _ in range(M)]
for i in range(M):
    fireballs[i][0] -= 1
    fireballs[i][1] -= 1
for _ in range(K):
    fireballs = move()

ans = 0
for i in range(len(fireballs)):
    ans += fireballs[i][2]
print(ans)
