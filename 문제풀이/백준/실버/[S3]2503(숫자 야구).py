'''
4
123 1 1
356 1 0
327 2 0
489 0 1
'''
import itertools, sys
input = sys.stdin.readline
N = int(input())
nums = list(itertools.permutations([x for x in range(1,10)], 3))
cnt = len(nums)
for j in range(N):
    number, s, b = map(int, input().split())
    check = [number//100, number//10%10, number%10]
    i = 0
    while i < len(nums):
        strike, ball = 0, 0
        test = nums[i]
        for k in range(3):
            if test[k] == check[k]:
                strike += 1
            elif test[k] in check:
                ball += 1
        if strike != s or ball != b:
            nums.remove(test)
            cnt -= 1
            continue
        i += 1         
print(cnt)