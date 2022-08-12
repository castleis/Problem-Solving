import sys
sys.stdin = open('input\\4408.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = []
    hall = [0]*200
    for _ in range(N):
        a = list(map(int,input().split()))
        # print(a)
        for i in range(2):
            if a[i] %2 :
                a[i] = a[i]//2 + 1
            else:
                a[i] //= 2
        # print(f'연산 후 : {a}')
        arr.append(a)
    for i in range(len(arr)):
        if arr[i][0] < arr[i][1]:
            for j in range(arr[i][0],arr[i][1]+1):
                hall[j-1] += 1
        else:
            for j in range(arr[i][1], arr[i][0]):
                hall[j-1] += 1
    # print(arr)
    # print(hall)
    print(f'#{t} {max(hall)}')