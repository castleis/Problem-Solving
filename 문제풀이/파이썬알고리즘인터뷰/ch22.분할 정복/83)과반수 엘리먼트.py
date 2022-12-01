# leetcode 169
class Solution:
    def majorityElement(self, nums):
        nums_set = list(set(nums))
        maxx = 0
        ans = 0
        for num in nums_set:
            val = nums.count(num)
            if maxx < val:
                maxx = val
                ans = num
        return ans
nums = [2,2,1,1,1,2,2]
a = Solution()
print(a.majorityElement(nums))

# Solution 1 : DP
from collections import defaultdict
def majorityElement1(nums):
    counts = defaultdict(int)
    for num in nums:
        if counts[num] == 0:            # 카운트되지 않은 숫자들만 카운트, 이미 카운트 한 숫자는 넘기기 => 최적화!
            counts[num] = nums.count(num)
        if counts[num] > len(nums)//2:
            return num

# Solution 2 : Divide and Conquer
def majorityElement2(nums):
    # 최소단위 리턴
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    # 분할
    a = majorityElement2(nums[:half])
    b = majorityElement2(nums[half:])

    # 정복 : b와 a 중에 절반 이상을 차지하는 숫자를 리턴
    return [b,a][nums.count(a) > half]