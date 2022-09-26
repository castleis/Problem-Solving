import sys
input = sys.stdin.readline

K,N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
start = 1
end = max(arr)
while start <= end :
    mid = (start + end) // 2
    lans = 0
    for i in arr:
        lans += i // mid
    # lans = sum([i//mid for i in arr])
    if lans >= N :
        start = mid + 1
    else:
        end = mid - 1

print(end)

# Solution
'''
start를 전체 랜선들의 합을 N으로 나눈 값을 지정해준다.
-> start = sum(arr)//N
그리고 while문 안의 for문을 한 줄로 나타낼 수 있다.(list comprehension)
-> lans = sum([i//mid for i in arr])
'''
    