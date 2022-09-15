import sys
sys.stdin = open('input/1232.txt')

def cal(n):
    if a[n] == '-':
        a[n] = cal(l[n]) - cal(r[n])
        return cal(l[n]) - cal(r[n])
    elif a[n] == '+':
        a[n] = cal(l[n]) + cal(r[n])
        return cal(l[n]) + cal(r[n])
    elif a[n] == '*':
        a[n] = cal(l[n]) * cal(r[n])
        return cal(l[n]) * cal(r[n])
    elif a[n] == '/':
        a[n] = cal(l[n]) / cal(r[n])
        return cal(l[n]) / cal(r[n])
    else:
        return a[n]


for t in range(1,11):
    N = int(input())
    a,l,r = [0]*(N+1),[0]*(N+1), [0]*(N+1)
    for _ in range(N):
        lst = list(input().split())
        if lst[1] in '+-*/':
            a[int(lst[0])] = lst[1]
            l[int(lst[0])] = int(lst[2])
            r[int(lst[0])] = int(lst[3])
        else:
            a[int(lst[0])] = int(lst[1])
    print(f'#{t} {int(cal(1))}')
