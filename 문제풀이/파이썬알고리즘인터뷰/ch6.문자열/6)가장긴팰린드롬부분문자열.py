# 0816 풀었던 알고리즘 문제에 적용해보기

string = input()
maxx = ''
for i in range(1,len(string)):
    for k in range(len(string)-i):
        new = ''
        for j in range(k,i+k+1):
            new += string[j]
        print(new)
        if new == new[::-1]:
            if len(new) > len(maxx):
                maxx = new
print(maxx)

# Sol1. 중앙을 중심으로 확장하는 풀이
'''다이나믹 프로그래밍으로도 풀 수 있다.(23장 참조)
여기서는 투 포인터가 중앙을 중심으로 확장하는 형태로 풀이 
-> 투 포인터가 슬라이딩 윈도우처럼 이동'''

def longestPalindrome(s):

    # 팰린드롬 판별 및 투 포인터 확장 함수
    def expand(left,right):
        # 윈도우를 중심으로 왼쪽과 오른쪽으로 포인터 확장, 
        # 확장한 위치가 서로 같은지 (팰린드롬인지) 확인
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 확장한 위치가 서로 같지 않으면 탐색한 문자열 return
        return s[left+1 : right]

    # 해당사항이 없을 때는 빠르게 리턴
    # 문자열 길이가 2보다 작거나 입력된 문자열 자체가 팰린드롬일 때
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 윈도우 이동 : 
    # expand(i,i+1): 2칸짜리 윈도우, expand(i,i+2): 3칸짜리 윈도우
    for i in range(len(s) - 1):
        result = max(result,expand(i,i+1),expand(i,i+2),key = len)
        
    return result