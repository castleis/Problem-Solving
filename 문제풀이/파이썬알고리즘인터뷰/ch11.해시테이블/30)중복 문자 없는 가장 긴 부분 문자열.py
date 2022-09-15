# 리트코드 3

def lengthOfLongestSubstring(s):
    start, end = 0,0
    maxx = 0
    dict = {}
    while end < len(s):
        print(s[end], start, end)
        if s[end] not in dict:
            dict[s[end]] = 1
            end += 1
        else:
            maxx = max(maxx, (end-start))
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    break
                dict.pop(s[start])
                start += 1
            dict.pop(s[end])
        print(dict, maxx)

    maxx = max(maxx,(end-start))
    return maxx


print(lengthOfLongestSubstring("tmmzuxt"))
"tmmzuxt"