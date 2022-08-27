# 방향성 그래프
import sys
sys.stdin = open('0818\\1219.txt')

def AtoB(v,graph):
    visited[v] = 1
    stack = [v]
    while stack:
        now = stack.pop()
        if now == 99:
            return 1
        else:
            for i in graph[now]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = 1

while True:
    try:
        t,n = map(int,input().split())
        s = list(map(int, input().split()))
        graph = [[] for _ in range(n+1)]
        for i in range(len(s)//2):
            graph[s[2*i]].append(s[2*i+1])
        visited = [0 for _ in range(100)]
        ans = AtoB(0,graph)
        if ans == 1:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    except:
        break
