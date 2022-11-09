# leetcode 122
class Solution:
    def maxProfit(self, prices):
        # 현재 위치에서 산다면 -> 이후의 값이 줄어들 때까지 배열에서 최고점을 찾기?
        # 1,3,5 -> (3-1) + (5-3) = (5-1) 개쩐당
        ans = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                ans += prices[i+1] - prices[i]
        return ans

prices = [1,2,3,4,5]
a = Solution()
print(a.maxProfit(prices))