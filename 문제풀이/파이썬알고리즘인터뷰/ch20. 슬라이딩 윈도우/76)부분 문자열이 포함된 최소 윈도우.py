# leetcode 76
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for char in t:
            if char in t_dict:
                continue
            t_dict[char] = t.count(char)
        # 윈도우 사이즈를 늘려가면서... 확인하기 => 모두 포함하는 윈도우를 찾으면 바로 return
        size = len(t)
        while True:
            for i in range(len(s)-size+1):
                # t를 포함하는지 어떻게 확인할거냐구 -> 같은 문자 중복되는 경우? in은 쓰면 안될듯
                # count를 써서.. 문자의 갯수가 같은지 확인해보기..?
                # window = s[i:i+size] 
                flag = True
                for char,count in t_dict.items():
                    if s[i:i+size].count(char) == count:
                        continue
                    else:
                        flag = False
                if flag:
                    return s[i:i+size]
            size += 1
s = "ADOBECODEBANC"
t = "ABC"
a = Solution()
print(a.minWindow(s,t))