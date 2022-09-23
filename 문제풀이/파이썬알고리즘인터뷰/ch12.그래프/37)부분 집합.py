# leetcode 78
# 73 ms ㅜㅜㅜ
class Solution:
    def subsets(nums):
        def combi(arr,k):
            result = []
            if k > len(arr):
                return result

            if k == 1:
                for i in arr:
                    result.append([i])

            elif k > 1:
                for i in range(len(arr)-k+1):
                    for j in combi(arr[i+1:], k-1):
                        result.append([arr[i]]+j)
            return result
        ans = [[]]
        for i in range(len(nums)+1):
            ans += combi(nums,i)
        return ans

nums = [1,2,3]
print(Solution.subsets(nums))