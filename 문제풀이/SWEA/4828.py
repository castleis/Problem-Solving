T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = 0
    min_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
    answer = max_num - min_num
    print(f'#{t} {answer}')