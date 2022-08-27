import sys
sys.stdin = open('0816\\4861.txt')

def girugi(arr):

    arr2 = []
    for i in range(N):
        cols = ''
        for j in range(N):
            cols += arr[j][i]
        arr2.append(cols)

    for i in range(N): # 행
        for j in range(N-M+1): # 열
            row = arr[i][j : j+M+1]
            if row == row[::-1]:
                return row

            col = arr2[i][j : j+M+1]
            if col == col[::-1]:
                return col


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(''.join(list(input())))
    result = girugi(arr)
    print(f'#{t} {result}')



