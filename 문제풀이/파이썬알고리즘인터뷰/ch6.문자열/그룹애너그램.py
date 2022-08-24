# 문자열 배열을 받아 애너그램 단위로 그룹핑하기
'''
["eat","tea","tan","ate","nat","bat"]
'''
arr = input()
setword = []

for word in arr:
    if set(word) not in setword:
        setword.append(set(word))

result = [[] for _ in range(len(setword))]
print(result)
for word in arr:
    for i in range(len(setword)):
        if set(word) == setword[i]:
            result[i].append(word)
print(result)