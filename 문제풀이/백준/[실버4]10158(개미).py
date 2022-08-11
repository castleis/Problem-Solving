'''
시간초과...!!! 0.15초만에 어떻게 하냐구!
# 1번
6 4
4 1
8
# 0 1

# 2번
6 4
5 3
4
# 3 1
'''
import sys
input = sys.stdin.readline

w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())
dx,dy = 1,1
cnt = min(w-x,h-y)
while cnt < t:
    x += dx * cnt
    y += dy * cnt
    if x == w and y == h :
        print('오른쪽 모서리에 부딪혔다!')
        dx = -dx
        dy = -dy
        cnt += min(w,h)
    elif x == y == 0 :
        print('왼쪽 모서리에 부딪혔다!')
        dx = -dx
        dy = -dy
        cnt += min(w,h)
    elif (x == w or x == 0) :
        print('위 or 아래에 부딪혔다!')
        dx = -dx
        cnt += min()
    elif (y == h or y == 0) :
        print('왼 or 오른쪽에 부딪혔다!')
        dy = -dy

print(x, y)
# print(f'마지막 위치 : {x},{y}')


    
# 병진님 풀이 -> 개미를 쭉~ 옮기고 나서 %W, %H 로 격자 안으로 집어넣어주고, %2로 위/아래, 왼/오 방향을 알려주는듯
W, H = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

a = (x+t) % W
b = (y+t) % H


if ((x+t)//W)%2 :
    a = W - a

if ((y+t)//H)%2 :
    b = H - b

print(a, b)