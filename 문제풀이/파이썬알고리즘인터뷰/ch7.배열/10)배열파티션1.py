# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력
'''
입력 : 1 4 3 2
출력 : 4
'''
nums = list(map(int,input().split()))
nums.sort()

'''
N개의 페어를 만들기 위한 작업
서로 다른 2개를 N번 뽑기
'''
