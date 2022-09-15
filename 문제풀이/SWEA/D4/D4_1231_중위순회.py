import sys
sys.stdin = open('1231.txt')

def pre(n):
    if n:
        pre(ch1[n])
        print(string[n], end='')
        pre(ch2[n])

for t in range(1,11):
    N = int(input())
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    string = [0]*(N+1)
    for _ in range(N):
        lst = list(input().split())
        if len(lst) == 4:
            string[int(lst[0])] = lst[1]
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
        elif len(lst) == 3:
            string[int(lst[0])] = lst[1]
            ch1[int(lst[0])] = int(lst[2])
        else:
            string[int(lst[0])] = lst[1]
    print(f'#{t}', end = ' ')
    pre(1)
    print()
    
