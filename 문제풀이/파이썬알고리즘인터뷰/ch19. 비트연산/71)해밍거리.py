# leetcode 461
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        xor_val = bin(x^y)
        for i in range(len(xor_val)):
            if xor_val[i] == '1':
                cnt += 1
        return cnt

# x = 1
# y = 4
# print(hammingDistance(x,y))