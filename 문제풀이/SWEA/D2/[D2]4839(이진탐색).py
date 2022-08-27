import sys
sys.stdin = open('0811/4839.txt')

def binary(p,i):
    start, end = 1,p
    cnt = 0

    while start <= end:
        mid = int((start+end)/2)
        cnt += 1
  
        if i == mid:
            return cnt
        elif i > mid :
            start = mid
        else:
            end = mid
    return cnt


T = int(input())
for t in range(1,T+1):
    P,a,b = map(int,input().split())

    A = binary(P,a)
    B = binary(P,b)

    if A < B :
        print(f'#{t} A')
    elif B < A :
        print(f'#{t} B')
    else:
        print(f'#{t} 0')

