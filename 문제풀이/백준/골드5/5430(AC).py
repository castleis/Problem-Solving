import sys
input = sys.stdin.readline
from collections import deque
def solve(F,N):
    R = 0
    for f in F:
        if f == 'R':
            R += 1
        if f == 'D':
            try:
                if R % 2:
                    N.pop()
                else:
                    N.popleft()
            except:
                return 'error'
    if N:
        if R % 2:
            N = N[::-1]
        N = str(N).replace(' ','')
    else:
        N = '[]'
    return N

T = int(input())
for t in range(1,T+1):
    F = list(input())
    n = int(input())
    if n == 0:
        a = input()
        N = []
    else:
        arr = input()
        arr1 = list(map(int, arr[1:len(arr)-2].split(',')))
        N = deque()
        for i in arr1:
            N.append(i)
    print(f'#{t} {solve(F,N)}')

'''
1

RRDD

7

[2,12,14,3,15,12,1]
'''