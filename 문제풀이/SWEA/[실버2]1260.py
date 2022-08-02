n,m,v = map(int,input().split())
a = []
#m동안 간선을 받고, 간선의 반대 방향도 함께 저장해줌
for i in range(m):
    a.append(list(map(int,input().split())))
    a.append(list(reversed(a[2*i])))
# 그래프의 모양을 만들 리스트
graph = [[] for i in range(n+1)]
#노드에 연결된 간선끼리 묶어 해당 노드의 인덱스에 추가
for i in range(len(a)):
    graph[a[i][0]].append(a[i])
#정렬을 해줌
for i in range(len(graph)):
    graph[i].sort()
print(f'graph : {graph}')

#노드를 방문했는지 여부를 저장할 리스트
visited = [False for i in range(n+1)]


def dfs(visited, graph, v, orders=[]):
    s = [v]
    #스택이 비어있지 않으면
    while s:
        #모든 노드를 방문했으면 break. @@@@@@@@@@여기가 좀 이상한듯!!!!!!!!!!!!
        if len(orders) == n:
            break
        # 방문순서 리스트 orders에 스택에 들어간 노드를 꺼내 저장해줌.
        orders.append(s.pop())
        print(f'방문 순서:{orders}')
        # 해당 노드를 방문했다고 바꾸고
        visited[v] = True
        # 인접리스트에 있는 간선들에 대해서
        for x,y in graph[v]:
            #이미 방문한 인접 노드이면 continue
            if visited[y] == True:
                continue
            #방문하지 않은 노드이면 스택에 추가하고 해당 노드로 재귀호출
            elif visited[y] == False :
                s.append(y)
                # print(f'방문여부 :{vtx_list}')
                # print(f'스택:{s}')
                dfs(visited, graph, y)
    #방문 순서 리스트를 return
    return orders
    
dfs(visited, graph,v)
