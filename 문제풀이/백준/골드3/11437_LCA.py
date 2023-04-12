import sys
from collections import deque
input = sys.stdin.readline

def make_tree(node):
    depth = 0
    queue = deque([node])
    is_checked_depth[node] = True
    node_depth[node] = depth
    while queue:
        node = queue.popleft()
        for neib in graph[node]:
            if not is_checked_depth[neib]:
                parent[neib] = node
                is_checked_depth[node] = True
                node_depth[neib] = node_depth[node] + 1
                queue.append(neib)

def make_parent_relation(node):
    depth_of_node = node_depth[node]
    # print(f'{node}번 노드의 깊이 -> {depth_of_node}')
    parent_relation[depth_of_node][node] = parent[node]
    for depth in range(depth_of_node-1, -1, -1):
        parent_relation[depth][node] = parent[parent_relation[depth+1][node]]
    return

def set_parent():
    max_depth = max(node_depth[x], node_depth[y])
    parent_relation[0] = parent
    for depth in range(1, max_depth):
        for node in range(1,node_cnt+1):
            parent_relation[node][depth] = parent_relation[parent[node][depth-1]][depth-1]

def LCA(x,y):
    # 부모 노드가 같아질 때까지 올라가기
    depth = max(node_depth[x], node_depth[y])
    print('노드의 깊이 : ', node_depth[x], node_depth[y])

    # print(f'depth = {depth}')
    while depth >= 0:
        print(f'============== {depth} -> {x},{y}')
        x = parent_relation[depth][x] if parent_relation[depth][x]!= 0 else x
        y = parent_relation[depth][y] if parent_relation[depth][y]!= 0 else y

        print(f'{depth}에서의 부모 : {x}, {y}')
        if x == y:
            return x
        else:
            depth -= 1

node_cnt = int(input())
is_checked_depth = [False] * (node_cnt + 1)
parent = [0] * (node_cnt + 1)
node_depth = [0] * (node_cnt + 1)
graph = [[] for _ in range(node_cnt+1)]
for _ in range(node_cnt - 1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

make_tree(1)  # 1번 노드, depth 0부터 시작
parent_relation = [[0]*(max(node_depth)+1) for _ in range(node_cnt+1)]
# print("parent : ",parent)
print("node_depth : ",node_depth)
for i in range(1,node_cnt+1):
    make_parent_relation(i)
print('parent_relation : ',parent_relation)
trial_cnt = int(input())
trial_nodes = [tuple(map(int,input().split())) for _ in range(trial_cnt)]

for x,y in trial_nodes:
    print(f'=================== [{x},{y}] ====================')
    print(LCA(x,y))