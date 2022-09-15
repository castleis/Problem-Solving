

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    tree = [0,]
    for i in arr:
        tree.append(i)
        idx = len(tree)-1
        while idx//2 > 0:
            if i < tree[idx//2]:
                tree[idx],tree[idx//2] = tree[idx//2],tree[idx]
            idx //= 2

    idx = len(tree)-1
    ans = 0
    while idx//2 > 0:
        ans += tree[idx//2]
        idx //= 2
    print(f'#{t} {ans}')

