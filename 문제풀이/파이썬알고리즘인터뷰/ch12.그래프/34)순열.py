# leetcode 46
import itertools

class Solution:
    def permute(self, nums):
        return list(itertools.permutations(nums))

# Solution
def permute1(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        print('================================')
        print(f'elements : {elements}')
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            print(f'elem : {e}')
            next_elements = elements[:] 
            next_elements.remove(e)
            print(f'next_elements : {next_elements}')

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
            print(f'prev : {prev_elements}')

    dfs(nums)
    return results           

nums = [1,2,3]
print(permute1(nums))