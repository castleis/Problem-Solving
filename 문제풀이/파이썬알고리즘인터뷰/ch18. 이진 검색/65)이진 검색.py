class Solution:
    def search(self, nums: List[int], target: int) -> int:
        S,L = 0, len(nums)-1
        while S <= L:
            mid = (S+L)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                L -= 1
            elif nums[mid] < target:
                S += 1
        return -1