def tree(lst):
    if lst:
        root = nums[lst[len(lst)//2]-1]
        s = lst[:len(lst)//2]
        l = lst[len(lst)//2+1:]
        if s:
            ch1[root] = nums[s[len(s)//2]-1]
            tree(s)
        if l:
            ch2[root] = nums[l[len(l)//2]-1]
            tree(l)
       

T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = [x for x in range(1,N+1)]
    root = N//2 + 1
    nodes = [0]*(N+1)
    print(nodes)
    nodes[1] = root
    ch1,ch2 = [0]*(N+1), [0]*(N+1)
    tree(nums)
    print(ch1,ch2)
    for i in range(1,N+1):
        if ch1[nodes[i]]:
            nodes[2*i] = ch1[nodes[i]]
        if ch2[nodes[i]]:
            nodes[2*i+1] = ch2[nodes[i]]
    print(nodes)
    print(f'#{t} {root} {nodes[N//2]}')


# =====================================================
# 중위 순회는 오름차 순이다!
# def tree(n):
#     global number
#     if n <= N:
#         tree(2*n)
#         trees[n] = number
#         number += 1
#         tree(2*n+1)

# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     number = 1
#     trees = [0]*(N+1)
#     tree(1)
#     print(f'#{t} {trees[1]} {trees[N//2]}')
