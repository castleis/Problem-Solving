N,M = map(int,input().split())
mapp = list(list(input()) for _ in range(N))
direction = {'U':(-1,0,'D'),'D':(1,0,'U'),'L':(0,-1,'R'),'R':(0,1,'L')}
visited = [[0]*M for _ in range(N)]
print(mapp)
# dfs로 연결되어 있는 곳을 같은 그룹으로 처리
# 그룹의 개수 => SAFE ZONE의 개수
# 그룹의 시작점과 끝 점이 같지 않을 수 있기 때문에 그룹의 중간에서 시작할 경우를 대비하여
# direction에 거꾸로 탐색을 위해 각 방향의 반대방향을 넣어둠.
def in_range(x,y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def make_group(i,j):
    stack = [(i,j)]
    visited[i][j] = 1
    while stack:
        x, y = stack.pop()
        dx, dy, reverse = direction[mapp[x][y]]
        nx, ny = x+dx, y+dy
        r_dx, r_dy, r_r = direction[reverse]
        r_nx, r_ny = x+r_dx, y+r_dy
        if in_range(nx,ny) and not visited[nx][ny]:
            stack.append((nx,ny))
        if in_range(r_nx, r_ny) and not visited[r_nx][r_ny]:
            if mapp[r_nx][r_ny] == reverse:
                stack.append((r_nx, r_ny))

    return