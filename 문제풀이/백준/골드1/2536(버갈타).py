from collections import defaultdict
'''
버스에 방향을 줘야댑니까??
하려고 하는 것 -> 특정 좌표에 어떤 버스가 지나가는지 보려구..
봐서 머함? -> 갈아탈 수 있는지 보려거,.,
왜???? -> 일단 가봐서 아니면 돌아오기 하려고..
어떻게~~~~~~~
딕셔너리 : 어떻게 쓰더라 ->  근데! 그럼 -1씩 안해줘도 되고.. 그냥 
리스트 : 3중 리스트 복잡합니더
ㅇ.ㅇ... ㅜㅡㅜ
'''

M,N = map(int,input().split())
K = int(input())
busMap = [[[] for _ in range(M+1)] for _ in range(N+1)]
# bus = [0]*(K+1)
for _ in range(K):
    b,x1,y1,x2,y2 = map(int,input().split())
    # bus[b] = [(x1,y1),(x2,y2)]
    if x1 == x2:
        if y2 < y1:
            y1,y2 = y2,y1
        for y in range(y1,y2+1):
            busMap[y][x1].append(b)
    elif y1 == y2:
        if x2 < x1:
            x1,x2 = x2,x1
        for x in range(x1,x2+1):
            busMap[y1][x].append(b)
sx,sy,dx,dy = map(int,input().split())   
end_bus = busMap[dy][dx]
graph = [[] for _ in range(K+1)]
for i in range(N+1):
    for j in range(M+1):
        if len(busMap[i][j]) <= 1:
            continue
        for k in busMap[i][j]:
            set_bus = set(busMap[i][j])
            set_k = set()
            set_k.add(k)
            # print(set_k)
            # print(set(busMap[i][j]) - set_k)
            graph[k] += list(set_bus - set_k)
for i in range(K+1):
    graph[i] = list(set(graph[i]))
print(graph)

def busta():
    ans = 1000000
    stack = busMap[sy][sx]
    for s in busMap[sy][sx]:
        print(f'====================== {s} =======================')
        visited = [0]*(K+1)
        stack = [s]
        while stack:
            print(f'stack : {stack}')
            bus = stack.pop()
            print(f'========== {bus} ===========')
            for b in graph[bus]:
                if b in end_bus:
                    ans = min(ans, visited[bus])
                    print(b, visited[bus])
                    print(visited)
                    return ans
                if not visited[b]:
                    stack.append(b)
                    visited[b] += visited[bus] + 1
                    break
print(busta())