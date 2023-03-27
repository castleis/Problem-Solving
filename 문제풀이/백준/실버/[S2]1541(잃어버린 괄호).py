'''
최솟값을 만들기 위해서는 -를 기준으로 괄호를 치면 됨.
'''

formula = input()
nums = formula.split('-')
if formula[0] == '-':
    answer = -int(nums[0])
answer = sum(map(int, nums[0].split('+')))
for i in range(1,len(nums)):
    sums = sum(map(int, nums[i].split('+')))
    answer -= sums
print(answer)