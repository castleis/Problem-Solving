import sys
sys.stdin = open('0818\\4871.txt')
# 문제를 눈 크게 뜨고 읽기 : 방향성 그래프였다 힘드넹
def path(s,g,graph):
    stack = [s]
    visited[s] = 1
    while stack : 
        v = stack.pop()
        if v == g :
            return True

        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                continue


T = int(input())
for t in range(1,T+1):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for i in range(e):
        x,y = map(int,input().split())
        graph[x].append(y)

    s,g = map(int,input().split())

    ans = path(s,g,graph)
    if ans :
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')