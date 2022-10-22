N,K = map(int,input().split())
A = [list(map(int,input().split()))]

S,E = 0, N-1
die = 0
R = []
while die < K:
    # 로봇 올리기, 현재 올리는 위치 내구도 -1, R리스트에 올라간 로봇의 위치 (현재 위치 S) 추가
    A[S] -= 1
    R[S] = S
    # 벨트가 한칸씩 회전
    S = (S-1) % (2*N)
    E = (E-1) % (2*N)
    # 로봇 한칸씩 옮기기
    for _ in range(len(R)):
        r = R.pop()
        nextt = (r+1)%2*N 
        if nextt <= E:
            if R[nextt] == 0 and A[nextt] > 0:
                R[nextt] = R[r]
                A[nextt] -= 1

