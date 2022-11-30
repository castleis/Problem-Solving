'''
교훈 : max 값을 정해둘 때는 무지성 1000000 때리지 말고 적당히 계산을 해보자
수없이 틀린 이유가 defual max 값을 잘못 잡아서 ㅋㅋ
'''
import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
max_height, min_height = 0,256
for i in range(N):
    for j in range(M):
        if mapp[i][j] > max_height:
            max_height = mapp[i][j]
        if mapp[i][j] < min_height:
            min_height = mapp[i][j]
T, H = sys.maxsize, 0
# max 값이 1000000 으로는 택도 없었나보다;
for h in range(min_height, max_height+1):
    tall_block,small_block = 0,0
    for i in range(N):
        for j in range(M):
            if mapp[i][j] >= h:
                tall_block += mapp[i][j] - h
            else:
                small_block += h - mapp[i][j]
    if tall_block + B >= small_block:
        time = tall_block * 2 + small_block
        if time <= T:
            T = time
            H = h
print(T, H)

'''
3 4 11
29 51 54 44
22 44 32 62
25 38 16 2

4 4 36
15 43 61 21
19 33 31 55
48 63 1 30
31 28 3 8

3 4 0
1 2 3 4
5 6 7 8
9 10 11 12
정답 : 57 6

1 3 99
0 0 1

1 3 4
0 0 0

1 3 4 
256 256 256
'''