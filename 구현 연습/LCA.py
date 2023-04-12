# 최소 공통 조상 알고리즘
'''
1. 각 노드의 level 정보를 파악
2. 공통 조상을 찾을 두 노드의 높이를 맞춰줌
3. 부모를 타고 거슬러 올라가면서 같은 부모를 만날때까지 반복
'''
node_cnt = int(input())
parent = [0] * (node_cnt + 1)
node_depth = [0]*(node_cnt+1)
is_checked_depth = [False] * (node_cnt+1)
graph = [[] for _ in range(node_cnt+1)]  # 노드들의 그래프 정보

for _ in range(node_cnt - 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def cal_depth(node, depth):
    is_checked_depth[node] = True
    node_depth[node] = depth
    for neib in graph[node]:
        if not is_checked_depth[neib]:
            parent[neib] = node
            cal_depth(neib, depth + 1)

def lca(a,b):
    # 1. 두 노드의 깊이를 맞춰준다
    while node_depth[a] != node_depth[b]:
        if node_depth[a] > node_depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    # 2. 부모를 타고 올라가면서 서로 같은 부모를 만날 때까지 반복
    while parent[a] != parent[b]:
        a = parent[a]
        b = parent[b]
    
    # 공통조상인 a (=b)를 리턴
    return a

# 개선된 LCA 알고리즘
'''
거슬러 올라가는 속도를 빠르게 만드는 방법
-> 2의 제곱 형태로 올라가게 만들기
DP를 사용해서 각 노드에 대해서 2^i 번째 부모에 대한 정보를 기록
즉 공간 복잡도를 늘리고 시간 복잡도를 줄이는 trade-off
'''
