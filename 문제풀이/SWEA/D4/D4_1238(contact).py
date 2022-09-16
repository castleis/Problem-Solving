import sys
sys.stdin = open('input/1238.txt')

def call(S):
    q = graph[S]
    visited = {}
    for i in q:
        visited[i] = True
    last = 0
    while q:
        last = max(q)
        for _ in range(len(q)):
            A = q.pop(0)
            if A in graph:
                for j in graph[A]:
                    if j not in visited:
                        q.append(j)
                        visited[j] = True
    return last

for t in range(1,11):
    L, S = map(int,input().split())
    graph = {}
    arr = list(map(int,input().split()))
    for i in range(L//2):
        if arr[2*i] not in graph:
            graph[arr[2*i]] = [arr[2*i+1]]
        else:
            graph[arr[2*i]].append(arr[2*i+1])
    print(f'#{t} {call(S)}')
