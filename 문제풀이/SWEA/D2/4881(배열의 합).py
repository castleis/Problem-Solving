def perm1(n,k,s):
    # global cnt
    global minV
    # cnt += 1
    # n번 인덱스가 원소의 개수와 같으면 min값과 비교한 후 리턴
    if n == k:
        if minV > s:
            minV = s
    # 가지치기!
    elif s >= minV:
        return 
    else:
        for i in range(n,k):
            print(f'{n}번째 행 : {s},{arr[n][p[n]]}')
            p[n],p[i] = p[i],p[n]
            # 현재 행에서 선택한 값을 먼저 더해서 다음 단계로 재귀
            perm1(n+1,k, s+arr[n][p[n]])
            p[i],p[n] = p[n],p[i]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    p = [i for i in range(N)]        # p[i] : i행에서 선택한 열 번호
    minV = 10*N
    # cnt = 0     # 함수가 몇번 호출되는지 확인해보자구~~
    # 순열 만들기
    perm1(0,N,0)
    print(f'#{t} {minV}')