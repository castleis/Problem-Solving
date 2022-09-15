
def cnt(n):
    global nodes
    if n:
        nodes += 1
        cnt(ch1[n])
        cnt(ch2[n])
    return nodes

T = int(input())
for t in range(1,T+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    ch1,ch2 = [0]*(E+2),[0]*(E+2)
    for i in range(E):
        p,c = arr[2*i], arr[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    nodes = 0
    print(f'#{t} {cnt(N)}')
