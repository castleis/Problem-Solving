nums = [4,5,6,7,0,1,2]
target = 0

class Solution:
    def search(self, nums, target):
        if target not in nums:
            return -1
        intial_idx = nums.index(target)
        nums.sort()
        S,L = 0, len(nums)-1
        while S <= L:
            idx = (S + L)//2
            if nums[idx] == target:
                if idx == intial_idx:
                    return idx
                return abs(idx - intial_idx)
            elif nums[idx] > target:
                L -= 1
            elif nums[idx] < target:
                S += 1

nums = [3,1]
target = 3
output = 1
answer = 0