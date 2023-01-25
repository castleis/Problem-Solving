'''
아이디어ㅓㅓㅓㅓㅓㅓ
1. 슬라이ㅣ드?딩 윈도우
2. split('') 개천재????? 아닌듯 ㅎㅎ;;
'''

for _ in range(int(input())):
    T, *nums = map(int,input().split())
    i,j = 0,1
    cnt = 0
    while j < 12:
        print(f'========= {i}, {j} ==========')
        flag = False
        print(nums[i], nums[j])
        if nums[j] <= nums[i]:
            print('??')
            i += 1
            if flag:
                print('cnt', cnt)
                cnt += 1
                j = i
        elif nums[j] > nums[i]:
            flag = True
        j += 1
        # print(i,j)
    print(f' cnt: {cnt}')