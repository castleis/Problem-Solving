import sys
sys.stdin = open('input/1240.txt')

T = int(input())
dictt = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,'0101111':6, '0111011':7, '0110111':8, '0001011':9}
for t in range(1,T+1):
    N,M = map(int,input().split())
    for _ in range(N):
        a = str(input().strip('0'))
        if len(a)//7 != 0:
            a = '0'*(7 - len(a)%7) + a
            arr = a
    L = len(arr)//7
    code = []
    for i in range(L):
        code.append(dict[arr[7*i:7*(i+1)]])
    if (sum(code[i] for i in range(8) if i%2 == 0)*3 + sum(code[i] for i in range(8) if i%2)) % 10 == 0:
        print(f'#{t} {sum(code)}')
    else:
        print(f'#{t} 0')
