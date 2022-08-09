import sys
sys.stdin = open('1945.txt')

T = int(input())
for t in range(1, T+1):
    a,b,c,d,e = 0,0,0,0,0
    n = int(input())
    while n > 1 : 
        if n % 2 == 0:
            a += 1
            n //= 2

        elif n % 5 == 0:
            c += 1
            n //= 5

        elif n % 7 == 0 :
            d += 1
            n //= 7

        elif n % 3 == 0 :
            b += 1
            n //= 3
    
        else : 
            e += 1
            n //= 11

    print(f'#{t} {a} {b} {c} {d} {e}')