# leetcode 455
class Solution:
    def findContentChildren(self, g, s):
        # g: 어린이, s: 쿠키~~
        # 쿠키가 처음부터 없으면 바로 0 리턴
        if not s:
            return 0
        # g는 역순, 쿠키는 오름차순 정렬
        g.sort(reverse=True)
        s.sort()
        i ,cnt = 0, 0               # i : g 인덱스  / cnt : 몇명을 만족하는지
        cookie = s.pop()            # 제일 큰 쿠키부터 누구한테 줄 수 있는지 확인할거임
        while i < len(g):           # 아이들의 수만큼 while 문을 돌건대
            if g[i] <= cookie:      # g가 쿠키보다 작거나 같으면 만족이므로 cnt += 1
                cnt += 1
                if s:               # 아이를 만족시켰으므로 다음 쿠키를 뽑을건데 남아있는 쿠키가 있으면 그거를 쓸거고
                    cookie = s.pop()
                else:               # 남아있는 쿠키가 없으면 0
                    cookie = 0
            i += 1                  # 다음 차례 아이의 g를 확인하러~
        return cnt

g = [1,2]
s = [1,2,3]
a = Solution()
print(a.findContentChildren(g,s))