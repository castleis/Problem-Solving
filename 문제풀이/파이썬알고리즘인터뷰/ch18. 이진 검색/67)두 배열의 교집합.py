class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        def binary_search(nums, target):
            S,L = 0, len(nums)-1
            while S <= L:
                idx = S + (L-S) // 2
                if nums[idx] == target:
                    ans.add(target)
                    return
                elif nums[idx] > target:
                    L -= 1
                elif nums[idx] < target:
                    S += 1
        nums2.sort()
        for target in nums1:
            binary_search(nums2,target)
        
        return list(ans)