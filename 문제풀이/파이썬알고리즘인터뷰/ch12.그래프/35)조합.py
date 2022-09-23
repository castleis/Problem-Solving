# leetcode 77
# 135ms~ 290ms (?)
class Solution:
    def combine(n, k):
        arr = [x for x in range(1,n+1)]
        def combi(arr,k):
            result = []
            if k > len(arr):
                return result

            if k == 1:
                for i in arr:
                    result.append([i])

            elif k > 1:
                for i in range(n-k+1):
                    for j in combi(arr[i+1:], k-1):
                        result.append([arr[i]]+j)
                        print(result)
            return result
        ans = combi(arr,k)
        return ans

print(Solution.combine(4,2))

# n = 4
# for i in range(1<<n):
#     nums = []
#     for j in range(n):
#         if i&(1<<j):
#             nums.append(j)
#     print(*nums)
# ==============================

# def recur(cur, p):            # 재귀를 통해 조합 생성
#     global ans, t
    
#     if cur == n + 1:
#         if is_connected():
#             ans = min(ans, abs(P - 2 * p))
#             t = True
#         return

#     ##########
#     part1.append(cur)
#     recur(cur + 1, p + population[cur])
#     part1.pop()

#     recur(cur + 1, p)