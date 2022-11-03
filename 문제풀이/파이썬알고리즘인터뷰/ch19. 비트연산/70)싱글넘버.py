# leetcode 136
class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for n in nums:  
            result ^= n
            # print(f'{n} : {result}')
        return result

nums = [4,1,2,1,2]
a = Solution()
a.singleNumber(nums)