'''
#1 4
#2 5
#3 7
'''
import sys
sys.stdin = open('0811/4836.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input()) # 색칠할 영역의 개수
    blue, red = [], []
    for _ in range(N):
        arr = list(map(int,input().split()))
        if arr[-1] == 1:
            red.append(arr)
        else:
            blue.append(arr)