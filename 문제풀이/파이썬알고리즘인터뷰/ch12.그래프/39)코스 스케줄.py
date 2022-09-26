# leetcode 207
import collections
class Solution:
    def canFinish(numCourses, prerequisites):
        visited = [0]*numCourses
        graph = collections.defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)
        
        def dfs(n):
            can = False
            stack = [n]
            visited[n] = 1
            while stack:
                course = stack.pop()
                for i in graph[course]:
                    if not visited[i]:
                        stack.append(i)
                        visited[i] = 1
            if sum(visited) == numCourses:
                can = True
            return can
        ans = dfs(0)
        return ans
numCourses = 2
prerequisites = [[1,0]]
print(Solution.canFinish(numCourses, prerequisites))

# Solution : DFS로 순환구조 판별!
# 순환 구조라면 False, 아니라면 True
def canFinish1(n,p):
    graph = collections.defaultdict(list)
    for x,y in p:
        graph[x].append(y)

    # 이미 방문한 노드를 저장할 집합 -> 이미 방문한 곳을 중복 방문하게 된다면 순환구조로 간주할 수 있음
    traced = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True

# Solution : 가지치기를 이용한 최적화
def canFinish2(n,p):
    graph = collections.defaultdict(list)
    for x,y in p:
        graph[x].append(y)

    # 이미 방문한 노드를 저장할 집합 -> 이미 방문한 곳을 중복 방문하게 된다면 순환구조로 간주할 수 있음
    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True