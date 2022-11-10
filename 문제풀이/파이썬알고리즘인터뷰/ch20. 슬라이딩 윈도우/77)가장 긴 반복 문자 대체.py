# leetcode 424
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 윈도우 크기는 1+k부터... 시작해도 될듯
        i,j = 0,0
        maxx = 0
        cnt = k
        for i in range(len(s)):
            print(f'============== {i} ============')
            for j in range(i,len(s)):
                print(f'=== {j}, {cnt} ===')
                if s[i] == s[j]:
                    j += 1
                else:
                    if cnt == 0:
                        print(f'끝  {j} => {j-i}')
                        maxx = max(maxx, (j-i))
                        cnt = k
                        break
                    cnt -= 1
            if cnt == 0:
                print(f'끝  {j} => {j-i+1}')
                maxx = max(maxx, (j-i+1))
                cnt = k
        return maxx
s = "ABAB"
k = 2
a = Solution()
print(a.characterReplacement(s,k))