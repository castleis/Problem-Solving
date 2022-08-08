import sys
sys.stdin = open('input.txt')
for x in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    ans = 0

    for i in range(2,N-2):
        a = arr[i-2:i+3]
        for _ in range(4):
            for j in range(4):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]

        if arr[i] == a[-1]:
            ans += (a[-1] - a[-2])
        else:
            continue
    print(f'#{x} {ans}')

