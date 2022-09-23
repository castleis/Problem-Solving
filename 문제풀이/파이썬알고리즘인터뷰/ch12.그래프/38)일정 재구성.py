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
