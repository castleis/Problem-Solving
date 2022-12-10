import sys
input = sys.stdin.readline
from itertools import combinations
def main():
    C = int(input())
    N = int(input())
    if C == 100:    # 가려는 채널이 현재 채널(100)과 같은 경우 0을 리턴
        return 0
    length = 0
    Num = C
    while C > 0:
        length += 1
        C //= 10
    if N == 0:      # 망가진 버튼이 없으면 가려는 채널의 자릿수만큼
        return length
    arr = list(map(int,input().split()))    # 망가진 버튼들 받기
    a_set = set(arr)
    nums = sorted(list(set(range(10)) - a_set))  # 안 망가진 버튼들
    nums_combi = combination(nums,length)
    # 안 망가진 버튼들의 조합을 구해보자
    print(f'정답 : {solve(Num, nums_combi)}')

def combination(nums, length):
    # combis = list(combinations(nums, length))
    # print(f'combis : {combis}')
    return

def solve(C,num):
    ch = []
    Num = C             # 원래 가려는 채널 보존해두기
    while C > 0:        # 가려는 채널 자릿수대로 나눠놓기
        print(C%10)
        ch.append(C%10) 
        C //= 10
    print(f'togo channel : {ch}')
    togo = []
    for number in ch:
        minn = sys.maxsize
        for i in num:
            if minn > (i-number):
                minn = (number-i)
        togo.append(i)
    print(togo)
main()