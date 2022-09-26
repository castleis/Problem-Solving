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