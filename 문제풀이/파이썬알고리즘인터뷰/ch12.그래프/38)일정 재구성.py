# leetcode 332
class Solution:
    def findItinerary(tickets):
        result = ['JFK']
        path = {}
        for i in range(len(tickets)):
            if tickets[i][0] not in path:
                path[tickets[i][0]] = [tickets[i][1]]
            else:
                path[tickets[i][0]] += [tickets[i][1]]
                path[tickets[i][0]].sort()
        print(path)
        stack = ['JFK']
        while stack:
            fromm = stack.pop()
            print(f'======{fromm}========')
            if fromm in path:
                for i in range(len(path[fromm])):
                    to = path[fromm][i]
                    if to != 0:
                        result.append(to)
                        stack.append(to)
                        path[fromm][i] = 0
                        break
                print(path)
            else:
                return result
        return result

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution.findItinerary(tickets))

# Solution
import collections
def findItinerary1(tickets):
    graph = collections.defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)
    
    # 어휘 순으로 방문하도록 sort
    for i in graph:
        graph[i].sort()
    '''
    위의 두 for문을 하나로 합치기
    for a,b in sorted(tickets):
        graph[a].append(b)
    '''

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    dfs('JFK')
    # 다시 뒤집어서 어휘 순으로 결과 출력
    return route[::-1]
'''
pop(0) vs pop()
pop(0) : O(n)
pop() : O(1)
따라서 입력값이 클 수록 pop()을 사용하는 것이 시간 복잡도를 줄이는 방법
이 문제에서 tickets를 처음부터 역순으로 정렬한다면 pop()으로 처리가 가능할 것.
'''