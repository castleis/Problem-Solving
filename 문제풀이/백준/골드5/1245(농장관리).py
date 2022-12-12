def solve():
    N,M = map(int,input().split())
    farm = [list(map(int,input().split())) for _ in range(N)]
    delta = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    visited = [[0]*(M) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:   # 방문하지 않은 곳이면 스택에 추가
                stack = [(i,j)]
                visited[i][j] = 1
                print(f'=========== farm[{i},{j}] : {farm[i][j]} ===========')
            else:
                continue
            flag = False
            while stack:
                x,y = stack.pop()
                now = farm[x][y]
                for di,dj in delta:         # 8방향을 살핌
                    ni,nj = x+di, y+dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if not visited[ni][nj]:         # 방문하지 않은 곳
                            print(f'farm[{ni},{nj}] : {farm[ni][nj]}')
                            if farm[ni][nj] == now:     # 현재 높이와 같으면 스택에 넣어주기, 방문처리
                                visited[ni][nj] = 1
                                stack.append((ni,nj))
                            elif farm[ni][nj] > now:    # 현재 높이보다 크면 산봉우리가 아니라는 뜻
                                flag = True
                            else:
                                visited[ni][nj] = 1
            print(flag)
            if not flag:    # 스택을 돌고 난 후, 나보다 높은 산봉우리가 없었다면 (flag = False) cnt 추가
                cnt += 1
                print(f'cnt : (+), {cnt}')
    return cnt

def main():
    answer = solve()
    return answer

print(main())