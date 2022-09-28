import heapq
import collections
class Solution:
    def findCheapestPrice(n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((w,v))
        Q = [(0,src,k)]
        while Q:
            price,node,k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                k -= 1
                for w,v in graph[node]:
                    alt = price + w
                    heapq.heappush((alt,v,k))
        return -1

def findCheapestPrice1(n,flights,src,dst,k):
    from collections import defaultdict
    from collections import deque
    
    graph = defaultdict(list)
    for s, e, p in flights:
        graph[s].append((e, p))
    
    queue = deque([(0, src, k)])
    min_price = [1e9] * n
    while queue:
        price, node, cnt = queue.popleft()
        if node == dst:
            continue
        if cnt >= 0:
            for e, p in graph[node]:
                if price + p < min_price[e]:
                    min_price[e] = price + p
                    queue.append((price + p, e, cnt - 1))
    
    if min_price[dst] == 1e9:
        return -1
    else:
        return min_price[dst]