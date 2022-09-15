import sys
sys.stdin = open('input/5178.txt')

T = int(input())
for t in range(1,T+1):
    N,M,L = map(int,input().split())
    arr = [0]*(2*N)
    for _ in range(M):
        n,num = map(int,input().split())
        arr[n] = num
    for i in range(N,0,-1):
        if arr[i] == 0:
            arr[i] = arr[2*i] + arr[2*i+1]
    print(f'#{t} {arr[L]}')