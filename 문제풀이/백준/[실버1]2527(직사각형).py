for _ in range(4):
    lst = list(map(int,input().split()))
    x,y = [],[]
    for i in len(lst):
        if i%2:
            y.append(lst[i])
        else:
            x.append(lst[i])
    if x[1] < x[2] or y[1] < y[2]:
        print('d')
    