def solve():
    nums = '0' + str(input())
    if nums[1] == '0':
        return 0
    length = len(nums)
    DP = [0]*(length)
    DP[0] = DP[1] = 1
    for i in range(2,length):
        if int(nums[i]) > 0:
            DP[i] += DP[i-1]
        if 10 <= int(nums[i-1]+nums[i]) <= 26:
            DP[i] += DP[i-2]
    return DP[-1]%1000000

print(solve())