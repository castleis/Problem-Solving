# 문자열을 뒤집는 함수를 작성. 리턴 없이 리스트 내부를 직접 조작.
'''
입력
["h","e","l","l","o"]
["H","a","n","n","a","h"]
'''
str1 = ["h","e","l","l","o"]
str2 = ["H","a","n","n","a","h"]
def swap(string):
    s = []
    for i in range(len(string)-1,-1,-1):
        s.append(string[i])
    return s
print(swap(str1))
print(swap(str2))

# Sol1. 투 포인터를 이용한 스왑
def reverseString(s) -> None:
    left,right = 0,len(s)-1
    # s = s[::-1] -> 리트코드에서는 오류 발생.
    # s[:] = s[::-1] ->
    while left < right :
        s[left],s[right] = s[right],s[left]
        left += 1
        right -=1
    return s
s = ["h","e","l","l","o"]
print(reverseString(s))

