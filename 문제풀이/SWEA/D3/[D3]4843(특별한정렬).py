import sys
sys.stdin = open('0811/4843.txt')

def sortt(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    s, e, l = [],[],[]
    for i in arr:
        if i < pivot:
            s.append(i)
        elif i > pivot :
            l.append(i)
        else :
            e.append(i)
    return sortt(s) + e + sortt(l)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    arr = sortt(arr)
    new = []
    for i in range(1,6):
        new.append(arr[-i])
        new.append(arr[i-1])
    print(f'#{t}', end=' ')
    print(*new)
