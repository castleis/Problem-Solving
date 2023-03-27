'''
아이디어ㅓㅓㅓㅓㅓㅓ
1. 슬라이ㅣ드?딩 윈도우
2. split('') 개천재????? 아닌듯 ㅎㅎ;;
'''

for _ in range(int(input())):
    cnt = 0
    T, *nums = map(int,input().split())
    # for num in nums:
    #     num = str(num-1)
    nums = [str(num-1) for num in nums]
    # print(nums)
    print('~~~~~~', T, '~~~~~~')
    print(nums)
    i = -1
    nums = ''.join(nums)
    while len(nums) > 0:
        nums = nums.split(str(i))
        print(nums)
        cnt += len(nums) - nums.count('')
        nums = ''.join(nums)
        print(f'{i} ====== {nums}')
        i += 1
    print('cnt :', cnt)