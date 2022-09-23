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
