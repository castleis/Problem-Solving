# 100x100 칸
# arr2를 구하지 않고 풀 수는 없을까? 시간이 오래 걸리는 것 같음!
import sys
sys.stdin = open('0816\\1216.txt')
input = sys.stdin.readline
for _ in range(10):
    t = int(input())
    arr = [''.join(list(input().strip())) for _ in range(100)]
    arr2 = [''.join(arr[j][i] for j in range(100)) for i in range(100)]
    maxx = 1

    for i in range(100):
        for k in range(maxx,100):
            for j in range(100-k):
                row = arr[i][j:j+k+1]
                if row == row[::-1]:
                    if k+1 > maxx:
                        maxx = k+1
                col = arr2[i][j:j+k+1]
                if col == col[::-1]:
                    if k+1 > maxx:
                        maxx = k+1
    print(f'#{t} {maxx}')

