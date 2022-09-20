# leetcode 46
class Solution:
    def permute(self, nums):
        result = [nums]
        def f():
            