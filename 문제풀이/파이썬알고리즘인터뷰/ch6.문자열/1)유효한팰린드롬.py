# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.
'''
입력 : "A man, a plan, a canal: Panama"
입력 : "race a car"
'''
def palindrom():
    sentence = input().lower()
    check = []
    for char in sentence:
        if char.isalnum():
            check.append(char)
    print(f'check : {check}')
    N = len(check)//2
    print(f'N : {N}')
    for i in range(N+1):
        print(f'{check[i]},{check[-(i+1)]} : {check[i]==check[-(i+1)]}')
        if check[i] != check[-(i+1)]:
            return False
    return True
print(palindrom())

# Sol1. 리스트로 변환, 304ms
def isPalindrome1(self,s:str) -> bool:
    strs = []
    for char in s:
        # .isalnum() 는 영문자, 숫자 여부를 판별하는 함수
        # 이를 이용해서 영문자, 숫자만 strs에 추가
        if char.isalnum():
            strs.append(char.lower())
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

#Sol2. 데크 자료형을 이용한 최적화, 64ms
'''deque를 선언함으로 속도 높이기'''
from collections import deque
def isPalindrome2(s):
    strs = deque()   # 머임?

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

#Sol3. 슬라이싱 사용, 36ms
def isPalindrome3(self, s:str) -> bool:
    s = s.lower()
    #정규식으로 불필요한 문자를 필터링
    s = re.sub('[^a-z0-9]', '',s)
    # [::-1]은 내부적으로 C로 뺘르게 구현되어 있어 1번보다 훨씬 좋은 속도를 기대할 수 있다.
    return s == s[::-1]