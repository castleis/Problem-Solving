import sys
sys.stdin = open('input/5658.txt')
for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    n = N//4
    # 중복을 제거하기 위해 집합을 선언
    num = set()
    nums = list(input())
    # 총 N//4번 회전하면 원래와 같아지므로 n번만 회전
    for _ in range(n):
        # 4개의 변에 있는 문자들을 하나의 문자열로 만들어 집합에 넣어주기
        for i in range(4):
            new = ''
            # 각 변에는 n개 만큼의 문자가 존재하므로 n번 반복
            for j in range(n):
                new += nums[n*i+j]
            num.add(new)
        # 첫번째 문자를 맨 뒤로 보내주기
        nums.append(nums.pop(0))
    num = list(num)
    result = []
    for char in num:
        # 16진수를 10진수로 바꾸기
        dec_val = int(char, base=16)
        result.append(dec_val)
    result.sort(reverse=True)
    print(f'#{t} {result[K-1]}')