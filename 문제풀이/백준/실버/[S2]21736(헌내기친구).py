import sys
from collections import deque
input = sys.stdin.readline

def main():
    def find_friends(x,y):
        cnt = 0
        que = deque([(x,y)])
        visited = [[0]*M for _ in range(N)]
        delta = [(1,0),(0,1),(-1,0),(0,-1)]
        while que:
            i,j = que.popleft()
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M:
                    if not visited[ni][nj]:
                        visited[ni][nj] = 1
                        if mapp[ni][nj] == 'P':
                            cnt += 1
                            que.append((ni,nj))
                        elif mapp[ni][nj] == 'O':
                            que.append((ni,nj))
        return cnt
    N,M = map(int,input().split())
    mapp = [list(input().strip()) for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if mapp[n][m] == 'I':
                ans = find_friends(n,m)
                if ans:
                    print(ans)
                else:
                    print('TT')
                quit()
main()
            