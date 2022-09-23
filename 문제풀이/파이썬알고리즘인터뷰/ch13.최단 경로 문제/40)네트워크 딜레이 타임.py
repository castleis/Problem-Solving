# leetcode 743

class Solution:
    def networkDelayTime(times, n, k):
        info = [[] for _ in range(n+1)]
        for time in times:
            x, *y = time
            info[x].append(y)
        # 각 정점을 방문했는지 체크할 리스트
        cnt = 1
        visited = [0]*(n+1)
        def dfs(k):
            # 스타트 지점은 999
            visited[k] = 999
            
            if info[k] == []:
                return cnt
                
            for x,y in info[k]:
                # 아직 방문하지 않은 정점이라면
                if not visited[x]:
                    print(f'방문할 정점 : {x}')
                    visited[x] = visited[k] + y
                    cnt += 1
                    dfs(x)
            return cnt
        result = dfs(k)
        if result == n:
            return max(visited)-999
        else:
            return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution.networkDelayTime(times,n,k))