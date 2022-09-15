# leetcode 771

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for s in stones:
            if s in jewels:
                cnt += 1
        return cnt
