N = int(input())
info = [tuple(map(int,input().split())) for _ in range(N)]
print(info)
D = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}
V = [[0]*101 for _ in range(101)]
pos = []
def rotate():
    global pos
    i,j,k = pos[-1]
    for n in range(len(pos)-1):
        x,y,d = pos[n]
        dx,dy = D[d % 4]
        pos.append((i+dx, j+dy, d%4))
        i,j = i+dx, j+dy
        V[i][j] = 1
    return
for x,y,d,g in info:
    pos.append((x,y,d))
    V[x][y] = 1
    for _ in range(g):
        rotate()
        print(pos)
ans = 0
for i in range(100):
    for j in range(100):
        if V[i][j] == V[i+1][j] == V[i][j+1] == V[i+1][j+1] == 1:
            ans += 1
print(ans)