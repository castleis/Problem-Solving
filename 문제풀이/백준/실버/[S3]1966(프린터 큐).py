def solve():
    order = 0
    importance_list = sorted(list(importance.values()))
    while paper:
        n = paper.pop(0)
        if importance[n] == importance_list[-1]:
            importance_list.pop()
            order += 1
            if n == M:
                return order
        else:
            paper.append(n)


for _ in range(int(input())):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    importance = {}
    paper = list(range(N))
    for i in range(N):
        importance[i] = arr[i]
    print(solve())