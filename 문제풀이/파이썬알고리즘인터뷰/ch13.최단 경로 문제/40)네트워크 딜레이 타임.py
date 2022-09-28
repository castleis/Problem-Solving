# leetcode 743
from collections import deque, defaultdict
import heapq

class Solution:
    def networkDelayTime(times, n, k):
        info = [[] for _ in range(n+1)]
        for time in times:
            u,v,w = time
            info[u].append((w,v))
        # 각 정점을 방문했는지 체크할 리스트
        def dfs(k):
            visited = [0]*(n)
            q = []
            q.append((0,k))
            while q:
                q.sort()
                time,m = q.pop(0)
                print(f'방문할 정점 : {m}')
                print(info[m])
                for t,x in info[m]:
                    # 아직 방문하지 않은 정점이라면
                    if not visited[x-1]:
                        visited[x-1] = time + t
                        q.append((visited[x-1],x))
                        print(f'visited : {visited}')
                        break
                print(f'q : {q}')
            return visited

        ans = dfs(k)
        return max(ans)

times = [[1,2,1],[2,3,2],[1,3,4]]
n = 3
k = 1
print(Solution.networkDelayTime(times,n,k))

# Solution
def networkDelayTime1(times,N,K):
    graph = defaultdict(list)

    for u,v,w in times:
        graph[u].append((v,w))
    # 큐에는 (소요시간, 정점) 순으로 담는다
    Q = [(0,K)]
    dist = defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time + w
                heapq.heappush(Q,(alt,v))
    
    if len(dist) == N:
        return max(dist.values())
    return -1

# Solution2
def networkDelayTime2(times,n,k):
    from collections import deque
    import sys
    inf = sys.maxsize

    adj_list = [[] for _ in range(n+1)]
    distance = [0] + [inf]*n
    distance[k] = 0
    for u,v,w in times:
        adj_list[u].append((v,w))
    
    dq = deque()
    dq.append((0,k))
    while dq:
        time, node = dq.popleft()
        for v,w in adj_list[node]:
            if time + w < distance[v]:
                distance[v] = time + w
                dq.append((time + w , v))
    result = max(distance)
    if result == inf:
        return -1
    else: return result