class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if numbers[i] > target:
                continue
            real_target = target - numbers[i]
            S, L = i+1, len(numbers)-1
            while S <= L:
                idx = (S + L) // 2
                if numbers[idx] == real_target:
                    return sorted([idx+1, i+1])
                elif numbers[idx] > real_target:
                    L -= 1
                elif numbers[idx] < real_target:
                    S += 1