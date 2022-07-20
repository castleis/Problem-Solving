T = int(input())
for t in range(1,T+1):
    k,n,m = input().split()
    k,n,m = int(k), int(n), int(m)
    charge_idx = list(map(int,input().split()))
    charge = [False]*(n+1)

    for i in range(n+1):
        if i in charge_idx:
            charge[i] = True
    bus = k
    for j in range(n+1):
        if 




