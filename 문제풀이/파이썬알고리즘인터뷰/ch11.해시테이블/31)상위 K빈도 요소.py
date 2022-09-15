# leetcode 347
def topKFrequent(nums,k):
    nums_set = set(nums)
    ans = {}
    if len(nums_set) <= k:
        return list(nums_set)
    for i in nums_set:
        ans[i] = nums.count(i)
    lst = sorted(ans.item(), key = lambda x : x[1])
    result = [lst[-1][1], lst[-2][1]]
    return result