from itertools import combinations as combi
import sys
input = sys.stdin.readline

def info():
    graph = [-1 for _ in range(N)]
    for i in range(N):
        a = list(map(int,input().split()))
        if a[0] == 0:
            graph[i] = []
        else:
            graph[i] = a[1:]
    return graph

def solve():
    ans = []
    for i in range(1,N//2+1):
        comb = list(combi(range(N), i))
        # print(f'comb : {comb}')
        for j in range(len(comb)):
            com1 = comb[j]
            com2 = list(set(range(N))-set(com1))
            # print(f'=============================')
            com1l = link(com1)
            com2l = link(com2)
            if not com1l == None and not com2l == None:
                # print(f'연결 통과 : {com1},{com2} -> {abs(com1l - com2l)}')
                ans.append(abs(com1l - com2l))
    # print(f'ans : {ans}')
    if not ans:
        return -1
    return min(ans)

def link(lst):
    visited = [0]*N
    q = [lst[0]]
    visited[lst[0]] = 1
    ans = popu[lst[0]]
    while q:
        a = q.pop(0)
        for b in graph[a]:
            if not visited[b-1] and b-1 in lst:
                q.append(b-1)
                visited[b-1] = 1
                ans += popu[b-1]
    for i in lst:
        if not visited[i]:
            return
    # print(lst, visited)
    return ans

N = int(input())
popu = list(map(int,input().split()))
graph = info()
print(f'graph : {graph}')
print(solve())

# 비트 연산자를 이용한 조합 구하기
# 기본
for i in range(1 << N):
    A, B, cnt = [], [], 0
    for j in range(N): 
        if i & (1 << j):
            cnt += 1
            A.append(j + 1)
        else:
            B.append(j + 1)
    if 0 < cnt < N:                       # A 구역의 개수가 1 ~ N-1개일 때만
        if check(A) and check(B):         # 각 구역끼리 모두 연결되어 있다면
            diff = min(compare(A), diff)  # 두 구역의 인구 수 차이 계산

# 부분 조합의 개수를 지정해주기 1 에서부터 1 << N-1 까지!
for i in range(1, 1 << N - 1):        # A 구역의 개수가 1 ~ N-1개일 때만
    A, B, cnt = [], [], 0
    for j in range(N): 
        if i & (1 << j):
            cnt += 1
            A.append(j + 1)
        else:
            B.append(j + 1)
    if check(A) and check(B):         # 각 구역끼리 모두 연결되어 있다면
        diff = min(compare(A), diff)  # 두 구역의 인구 수 차이 계산
