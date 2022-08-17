import sys
sys.stdin = open('0816\\3143.txt')

def nextt(b):
    B = len(b)
    next = [0]*B
    j = 0
    for i in range(1,B):
        if b[i] == b[j]:
            j += 1
            next[i] = j
        else:
            j = 0
            if b[i] == b[j]:
                j += 1
                next[j] = j
    return next

def KMP(a,b):
    num = 0
    A = len(a)
    B = len(b)
    next = nextt(b)
    i,j = 0,0
    while i < A :
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            if j != 0 :
                j = next[j-1]
            else:
                i += 1

        if j == B :
            num += 1
            j = 0
    ans = A + (1-B)*num
    return ans

T = int(input())
for t in range(1,T+1):
    a,b = input().split()
    print(f'#{t} {KMP(a,b)}')

