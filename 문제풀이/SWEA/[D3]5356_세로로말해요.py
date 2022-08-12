import sys
sys.stdin = open('input\\5356.txt')

T = int(input())
for t in range(1,T+1):
    arr = []
    maxx = 0
    for _ in range(5):
        a = input()
        if maxx < len(a):
            maxx = len(a)
        arr.append(a)
    new = ''
    for i in range(maxx):
        for j in range(5):
            if len(arr[j]) <= i:
                pass
            else:
                new += arr[j][i]
    print(f'#{t} {new}')
