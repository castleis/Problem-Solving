import sys

sys.stdin = open('input\1208.txt')

def quick_sort(arr):
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
    return quick_sort(s) + e + quick_sort(l)

def dumps(arr, dump):
    # dump가 0이 될때까지 수행
    while dump > 0 :
        # arr를 오름차순으로 정렬
        arr = quick_sort(arr)
        # 최댓값에서 -1, 최솟값에 +1
        arr[-1] -= 1
        arr [0] += 1
        # 한번 시행할 때마다 주어진 dump를 -1
        dump -= 1
    # 마지막으로 다시 한번 정렬
    arr = quick_sort(arr)
    # 최댓값, 최솟값의 차이를 return합니다.
    return arr[-1] - arr[0]

for t in range(1,11):
    dump = int(input())
    arr = list(map(int, input().split()))
    print(f'#{t} {dumps(arr,dump)}')

