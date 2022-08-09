
T = int(input())
for t in range(1,T+1):
    n,q = map(int,input().split())
    arr = [0]*n

    # 1
    for i in range(q):
        L, R = map(int,input().split())
    
        for j in range(L,R+1):
            arr[j-1] = i+1

    # 2 틀림 ㅠㅠㅠ ================================================
    # 뒤에서부터 거꾸로 탐색합니다.
    a = []
    for _ in range(q):
        a.append(list(map(int,input().split())))
    print(a)
    for i in range(q-1,-1,-1):
        # 처음에는 주어진 L부터 R까지의 값을 바꿔줍니다.
        if i == q-1:
            print(a[i][0], a[i][1])
            for j in range(a[i][0], a[i][1]+1):
                arr[j-1] = i+1
        # 그 다음부터는 지금의 R과 이후의 L을 비교합니다.
        else :
            # i번째 R이 i+1번째 L보다 크다면 i+1번째 L까지만 값을 바꿉니다.
            if a[i][1] >= a[i+1][0]:
                for j in range(a[i][0],a[i+1][0]):
                    arr[j-1] = i+1
            # 아니라면 i번째의 R부터 L까지의 값을 바꿉니다.
            else:
                for j in range(a[i][0], a[i][1]+1):
                    arr[j-1] = i+1
    # ===========================================================
    print(f'#{t}', end =' ')
    for k in arr :
        print(k, end =' ')
    