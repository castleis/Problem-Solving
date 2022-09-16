from itertools import combinations as comb
import sys
sys.stdin = open('input/4012.txt')

def skill(com):
    power = 0
    for p1,p2 in comb(com,2):
        power += ingredients[p1][p2] + ingredients[p2][p1]
    return power

T = int(input())
for t in range(1,T+1):
    N = int(input())
    ingredients = [list(map(int,input().split())) for _ in range(N)]
    result = []
    minn = 1000000
    for com in comb(range(N),N//2):
        com1 = com
        com2 = list(set(range(N)) - set(com1))
        power1 = skill(com1)
        power2 = skill(com2)
        if abs(power1-power2) < minn:
            minn = abs(power1-power2)
    print(f'#{t} {minn}')