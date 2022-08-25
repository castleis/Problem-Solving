# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력
'''
입력 : -1 0 1 2 -1 -4
출력 : [-1,0,1],[-1,-1,2]
'''
arr = list(map(int,input().split()))
def sol(arr):
    arr.sort()
    print(arr)
    result = []
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            print(arr[i],arr[left],arr[right])
            res = arr[i] + arr[left] + arr[right]
            print(res)
            if res == 0:
                result.append([arr[i],arr[left],arr[right]])
                break
            elif res < 0 :
                left += 1
            else:
                right -= 1
    return result    
print(sol(arr))


# Sol 투포인터로 계산
def threeSum1(nums):
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        # 기준값이 이전과 같다면 스킵 (중복처리)
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left,right = i+1, len(nums)-1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            # sums가 0보다 작다면, nums[left]가 너무 작다는 뜻이므로 left += 1
            # sort 되어 있으므로 오른쪽 값이 왼쪽보다 크다!
            if sums < 0:
                left += 1
            # 마찬가지로 0보다 크다면 nums[right]가 너무 크다는 뜻이므로 right -= 1
            elif sums > 0:
                right -= 1
            # sums가 0이라면 
            else:
                results.append(nums[i],nums[left],nums[right])
                # 다음 계산을 위해 중복되는 구간을 건너뛰기
                # left가 right보다 작을때만
                # nums[left] 값이 다음 nums[left]과 같은 동안 left += 1
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # nums[right]값이 다음 nums[right]과 같은 동안 right -= 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return results

# Sol 브루트포스로 계산
def threeSum2(nums):
    result = 0
    # 앞뒤로 같은 값이 있을 경우, 이를 쉽게 처리하기 위해 정렬
    nums.sort()

    # 첫번째 포인터
    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 두번째 포인터
        for j in range(i+1, len(nums)-1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            # 세번째 포인터
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                # 세 포인터의 합이 0인지 확인
                if nums[i]+nums[j]+nums[k] == 0:
                    result.append([nums[i],nums[j],nums[k]])
    return result