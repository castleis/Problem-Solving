# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴
# 이 문제는 매우 쉽지만! 최적화할 수 있는 방법이 여러가지가 숨어있어서 코딩 인터뷰 시 높은 빈도로 출제되는 문제
'''
입력 
nums = [2,7,11,15], target = 9
출력
[0,1]
'''

nums = list(map(int,input().split()))
target = int(input())

def sol(nums,target):
    for i in range(len(nums)):
        if target-nums[i] in nums:
            return [i,nums.index(target-nums[i])]
result = sol(nums,target)
print(result)

# Sol1. 브루트 포스로 계산 
'''
시간복잡도 : O(n^2)
'''
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# Sol2. in 을 이용한 탐색
'''
in의 시간 복잡도는 O(n)
'''
def twoSum2(nums,target):
    for i,n in enumerate(nums):
        complement = target - n
    # 왜 범위를 [i+1:]로 주는지???
    if complement in nums[i+1:]:
        # nums.index(n) 말고 그냥 i를 return하면 되는 것 아닌지???????
        return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

#Sol3. 첫번째 수를 뺀 결과 키 조회
'''
딕셔너리는 해시 테이블로 구현되어 있어 키를 이용하여 조회한다면 평균적으로 O(1)에 조회할 수 있다.
'''
def twoSum3(nums,target):
    nums_map = {}
    for i,num in enumerate(nums):
        # 값을 key로, 인덱스를 value로 딕셔너리에 저장
        nums_map[num] = i

    for i,num in enumerate(nums):
        # 타겟에서 첫번째 수를 뺀 결과가 딕셔너리의 키로 존재하고, 자기자신이 아닐때?
        if target-num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# Sol4. 조회구조 개선


# Sol5. 투 포인터 이용


# Sol6. 고(Go) 구현