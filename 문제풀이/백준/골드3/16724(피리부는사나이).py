# 그룹의 개수 => SAFE ZONE의 개수
N,M = map(int,input().split())
mapp = list(list(input()) for _ in range(N))
direction = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
visited = [[0]*M for _ in range(N)]
rep = [i for i in range(N*M)]
def find(i):
    if rep[i] != i:
        return find(rep[i])
    return i

def union(i,j):
    i = find(i)
    j = find(j)

    if i < j:
        rep[j] = i
    else:
        rep[i] = j
    return

def in_range(x,y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

# 그룹 지어주기 -> find_union
for i in range(N):
    for j in range(M):
        dir = mapp[i][j]
        di, dj = direction[dir]
        ni, nj = i+di, j+dj
        union(i*M+j, ni*M+nj)


# 그룹 개수 count
ans = 0
for i in range(N*M):
    if i == find(i):
        ans += 1
print(ans)