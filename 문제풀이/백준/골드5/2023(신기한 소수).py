import math
# 소수인지 판별해줄 함수
def is_prime(n):
    for k in range(2,int(math.sqrt(n)+1)):
        if n % k == 0:
            return False
    return True

# i번째 자리의 수를 결정해서 소수만 남겨 리턴하는 함수
# num_list는 i-1번째 자리까지 정해진 소수들의 리스트
def num_pos(num_list):
    new_num_list = []
    for num in num_list:
        # k가 i번째 자리에 들어갈 숫자
        for k in odd_num:
            new_num = int(str(num) + str(k))
            # i번째 자리에 k를 넣었을 때, 소수라면 new_num_list에 추가
            if is_prime(new_num):
                new_num_list.append(new_num)
    return new_num_list

N = int(input())
odd_num = [1,3,5,7,9]
# 소수로 판별된 숫자를 넣어줄 리스트
# 첫 숫자는 2,3,5,7
num_list = [2,3,5,7]
for _ in range(N-1):
    num_list = num_pos(num_list)
# 마지막으로 남은 num_list가 N자리수의 소수들의 리스트
for number in num_list:
    print(number)