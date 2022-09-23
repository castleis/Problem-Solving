# leetcode 39
class Solution:
    def combinationSum(candidates, target):
        N = len(candidates)
        ans = []
        for i in range(1 << N):
            result = []
            for j in candidates:
                if i & (1 << j):
                    result.append(j)
                    print(j)
            print(f'result : {result}')
            # print(result[-1], sum(result[-1]))
            # if result and sum(result[-1]) == target:
            #     ans.append(result[-1])
        return ans
candidates = [2,3,6,7]
target = 7
print(Solution.combinationSum(candidates, target))