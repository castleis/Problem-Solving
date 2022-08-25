# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력
# 아니 근데 나눗셈을 하지 말래...@.@
'''
입력 : 1 2 3 4
출력 : [24,12,8,6]
'''
nums = list(map(int,input().split()))
def solve(nums):
    result = []
    maxx = 1
    for i in nums:
        maxx *= i

    for i in nums:
        result.append(maxx//i)
    return result
print(solve(nums))

def sol(nums):
    result = []
    for i in range(len(nums)):
        num = 1
        for j in range(len(nums)):
            if j == i:
                continue
            else:
                num *= nums[j]
        result.append(num)
    return result
print(sol(nums))

# Sol1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
