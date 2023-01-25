# 감자.. ㅜㅜ
import sys
input = sys.stdin.readline
delta = [(0,1),(-1,0),(0,-1),(1,0)]
for _ in range(int(input())):
    orders = list(input())
    X,Y = 0,0
    b_x, b_y, s_x, s_y = 0, 0, 0, 0
    d = 0
    for order in orders:
        if order == 'F':
            X += delta[d][0]
            Y += delta[d][1]
        elif order == 'B':
            X += delta[(d+2)%4][0]
            Y += delta[(d+2)%4][1]
        elif order == 'L':
            d = (d+1) % 4
        elif order == 'R':
            d = (d+3) % 4

        b_x = max(X, b_x)
        b_y = max(Y, b_y)
        s_x = min(X, s_x)
        s_y = min(Y, s_y)
    print(abs(b_x - s_x) * abs(b_y - s_y))
    