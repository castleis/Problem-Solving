#카운팅 정렬을 따라해보았다.
T = int(input())
for t in range(1,T+1):
    N = int(input())
    a = input()
    a_lis = []
    max_num = 0
    max_cnt = 0
    for i in range(len(a)):
        a_lis.append(a[i])
    a_list = list(map(int, a_lis))
    count = [0]*(max(a_list)+1)
    for j in range(len(a_list)):
        count[a_list[j]] += 1
    for k in range(len(count)):
        if count[k] >= max_cnt:
            max_cnt = count[k]
            max_num = k
    print(f'#{t} {max_num} {max_cnt}')
