N = int(input())
info = [tuple(map(int,input().split())) for _ in range(N)]
print(info)
D = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}
def rotate(center, pos):
    X,Y = center
    for n in range(len(pos)):
        i,j = pos[n]
        if i < X and j < Y:
            i = 2*X-i
            pos.append((i,j))
        elif i > X and j < Y:
            j = 2*Y-j
            pos.append(i,j)
        
    return
for x,y,d,g in info:
    pos = [(x,y)]
    dx,dy = D[d]
    center = (x+dx, y+dy)  # 0세대 좌표
    rotate(center, pos)