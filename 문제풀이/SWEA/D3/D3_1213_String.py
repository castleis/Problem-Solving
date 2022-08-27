import sys
sys.stdin = open('0812\\1213.txt')

def searchh(P,T):
    lP = len(P)
    lT = len(T)
    i = 0
    cnt = 0
    while i <= (lT-lP) :
        if T[i : i+lP] == P:
            cnt += 1

        i += 1
    return cnt
    
for _ in range(10):
    t = input()
    P = input() # pattern
    T = input() # target
    ans = searchh(P,T)
    print(f'#{t} {ans}')
