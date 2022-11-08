# leetcode 239
class Solution:
    def maxSlidingWindow(self, nums, k):
        arr = []
        for i in range(len(nums)-k):
            arr.append(max(nums[i:i+k]))
        return arr