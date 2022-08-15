import sys
input = sys.stdin.readline
'''
간선의 갯수를 구해야 하는 걸까~~~ 구한다면 어떻게 구해야하는 걸까~~~
DFS로 구하는것이 어떨까!
'''
N = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[]for _ in range(N+1)]
for _ in range(m):
    p,c = map(int,input().split())
    graph[p].append(c)
    graph[c].append(p)
print(graph)
visited = [0]*(N+1)
# for i in range(len(graph)):
#     graph[i].sort(reverse = True)
stack = [a]
visited[a] = 1
print(a,b)
def relation(a,b,graph,how_long = 0, find = False):
    while stack:
        print(f'stack : {stack}')
        here = stack.pop()
        for i in graph[here]:
            print(f'현재({here})의 인접노드: {graph[here]}')

            if b in graph[here]:
                print('발견!')
                find = True
                return how_long+1
            
            elif not visited[i]:
                stack.append(i)
                visited[i] = 1
                how_long += 1
                print(f'촌수 : {how_long}')
                relation(a,b,graph)
        how_long -= 1
        print(f'촌수-1 : {how_long}')
    if find == False:
        return -1       
print(relation(a,b,graph))

