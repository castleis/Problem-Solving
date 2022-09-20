# leetcode 17
class Solution:
    def letterCombinations(self, digits):
        nums = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        
        def f(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)):
                for j in nums[digits[i]]:
                    f(i+1,path+j)

        result = []
        f(0,'')

        return result