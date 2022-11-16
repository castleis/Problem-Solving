# leetcode 455
class Solution:
    def findContentChildren(self, g, s):
        # g: 어린이, s: 쿠키~~
        g.sort()
        s.sort()
        ranges = min(len(g),len(s))
        for i in range(ranges):
            if g[i] > s[i]:
                return len(g[:i])
        return len(g)

g = [1,2]
s = [1,2,3]
a = Solution()
print(a.findContentChildren(g,s))