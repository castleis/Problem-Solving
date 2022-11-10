# leetcode 424
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k = 0인 경우, s가 모두 같은 문자인 경우, 마지막 문자 처리
        maxx = 0
        뇌절금지 = []       # 비교할 문자 필터링하는 용도
        for start in range(len(s)):
            i,j =  0,0
            char = s[start]
            if char in 뇌절금지:
                continue
            else:
                뇌절금지.append(char)
            while j < len(s):
                j += 1
                # print(f'====== {i}, {j} ======')
                window = s[i:j]
                # print(window.count(s[i]))
                if (j - i - window.count(char)) <= k:
                    # print('뀨')
                    maxx = max(maxx, (j-i))
                # 현재 윈도우 크기(j-i) 에서 기준 문자(s[i])의 갯수를 뺀 값이 k보다 크다면
                # 어차피 다 바꿔도 안돼~~~~~~
                # 그니까... i를 증가시켜주자
                elif (j - i - window.count(char)) > k:
                    i += 1
        return maxx

# s = "ABAB"
# s = "AAAB"
s = "AAAA"
k = 2
k = 0
a = Solution()
print(a.characterReplacement(s,k))