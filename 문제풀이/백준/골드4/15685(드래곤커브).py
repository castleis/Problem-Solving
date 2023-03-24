N = int(input())
D = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}
V = [[0]*101 for _ in range(101)]

for _ in range(N):
    x,y,d,g = map(int,input().split())
    V[y][x] = 1
    x,y = x+D[d][0], y+D[d][1]
    V[y][x] = 1
    pos = [(d+1)%4]
    # 1~g 세대 커브를 만들어주기
    for _ in range(g):
        next = []
        for d in pos[::-1]:
            dx,dy = D[d]
            x, y = x+dx, y+dy
            next.append((d+1)%4)
            V[y][x] = 1
        pos += next
ans = 0
for i in range(100):
    for j in range(100):
        if V[i][j] == V[i][j+1] == V[i+1][j] == V[i+1][j+1] == 1:
            ans += 1
print(ans)
