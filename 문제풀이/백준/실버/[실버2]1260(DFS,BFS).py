from collections import deque
n,m,v = map(int,input().split())
# 그래프의 모양을 만들 리스트
graphs = [[] for i in range(n+1)]
a = []
#m동안 간선을 받고, 간선의 반대 방향도 함께 저장해줌
for i in range(m):
    a.append(list(map(int,input().split())))
    a.append(list(reversed(a[2*i])))
#노드에 연결된 간선끼리 묶어 해당 노드의 인덱스에 추가
for i in range(len(a)):
    graphs[a[i][0]].append(a[i])
#정렬을 해줌 (작은 노드부터 순회하기 위함)
for i in range(len(graphs)):
    graphs[i].sort()
# print(f'graph : {graphs}')
s = [v]

class Aaa:
    def __init__(self,n):
        #노드를 방문했는지 여부를 저장할 리스트
        self.visited = [False for i in range(n+1)]
        self.visited[0] = True

    #dfs 탐색
    def dfs(self,graphs,v,s,orders=[]):
        self.visited[v] = True
        #스택이 비어있지 않으면
        while s:
            
            # 방문순서 리스트 orders에 스택에 들어간 노드를 꺼내 저장해줌.
            i = s.pop()
            # print(f'방문 : {i}')
            orders.append(i)
            # print(f'방문 순서:{orders}')

            #모든 노드를 방문했으면 break.
            if False not in self.visited:
                break

            # 인접리스트에 있는 간선들에 대해서
            for x,y in graphs[i]:
                # print(f'다음 방문 :{y}')
                #방문하지 않은 노드라면 스택에 추가하고 해당 노드로 재귀호출
                if self.visited[y] == False :
                    s.append(y)
                    self.visited[y] = True
                    
                    # print(f'방문여부 :{self.visited}')
                    # print(f'스택:{s}')
                    Aaa.dfs(self,graphs,y,s)
                else :
                    continue
        #방문 순서 리스트를 return
        return orders


    #bfs 탐색
    def bfs(self,graphs,v):
        orders=[]

        queue = deque([v])
        self.visited[v] = True
        # queue가 빌때까지
        while queue:
            # print(f'queue : {queue}')
            # 큐에서 맨 앞 숫자를 꺼내 orders에 추가
            n = queue.popleft()
            orders.append(n)
            # print(n)

            # n의 인접리스트에 있는 i들에 대해서
            for x,i in graphs[n]:
                # i번째에 방문하지 않았다면
                if not self.visited[i]:
                    # 방문했다고 바꾸고 큐에 해당 숫자 넣어주기
                    self.visited[i] = True
                    queue.append(i)
                else:
                    continue
            # print(f'방문순서 : {orders}')
            # print(f'방문여부 : {self.visited}')
        return orders
dfs_a = Aaa(n)
bfs_a = Aaa(n)
print(f'dfs : {dfs_a.dfs(graphs,v,s)}')
print(f'bfs :{bfs_a.bfs(graphs,v)}')


# 백준 1등 코드
import sys
N,M,V = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]

for __ in range(M):
    n1,n2 = map(int, sys.stdin.readline().split())
    # 내가 한거보다 이렇게이렇게이렇게 깔끔할수 잇따니 정말정말정말정말 대단하다
    edge[n1].append(n2)
    edge[n2].append(n1)

for e in edge:
    e.sort(reverse=True) # why reverse? : dfs를 쉽게 해주려구

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]  # why edge[v1] : 인접 노드들을 한번에 넣어준다. EDGE가 reverse로 정렬되어있기 때문에 순서가 작은 노드부터 pop된다!
    return d_visit

def bfs():
    b_visit = []
    b_check = [0 for _ in range(N+1)]
    queue = [V]
    b_check[v] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue # 순서에 의미가 있다아ㅏ아ㅏㅏ
    return b_visit

print(' '.join(map(str,dfs())))
print(' '.join(map(str,bfs())))
