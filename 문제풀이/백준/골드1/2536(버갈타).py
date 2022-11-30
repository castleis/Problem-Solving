def busta(bus,cnt):
    global minn, visited
    if cnt > minn:
        visited[bus-1] = 0
        print(visited)
        return
    for b in graph[bus]:
        if b in end_bus and not visited[b-1]:
            minn = min(minn, cnt)
            return 
        if not visited[b-1]:
            visited[b-1] = 1
            print(visited)
            busta(b, cnt+1)

M,N = map(int,input().split())
K = int(input())
busMap = [[[] for _ in range(M+1)] for _ in range(N+1)]
graph = [[] for _ in range(K+1)]
for _ in range(K):
    b,x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2:
        if y2 < y1:
            y1,y2 = y2,y1
        for y in range(y1,y2+1):
            if busMap[y][x1]:
                for bus in busMap[y][x1]:
                    graph[bus].append(b)
                    graph[b].append(bus)
            busMap[y][x1].append(b)
    elif y1 == y2:
        if x2 < x1:
            x1,x2 = x2,x1
        for x in range(x1,x2+1):
            if busMap[y1][x]:
                for bus in busMap[y1][x]:
                    graph[bus].append(b)
                    graph[b].append(bus)
            busMap[y1][x].append(b)
sx,sy,dx,dy = map(int,input().split())   
end_bus = busMap[dy][dx]

print(f'graph : {graph}')
print(f'end_bus : {end_bus}')
minn = 100000
Bus = busMap[sy][sx]

for bus in Bus:
    visited = [0]*K
    visited[bus-1] = 1
    busta(bus,0)
print(minn)