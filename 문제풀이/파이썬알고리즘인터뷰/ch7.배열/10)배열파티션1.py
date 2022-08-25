# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력
'''
입력 : 1 4 3 2
출력 : 4
'''
nums = list(map(int,input().split()))
nums.sort()
maxx = 0
for i in range(0,len(nums),2):
    maxx += min(nums[i],nums[i+1])
print(maxx)

# Sol1. 오름차순 풀이
def arrayPairSum(nums):
    