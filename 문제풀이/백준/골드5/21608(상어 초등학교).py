def where(I):
    # 좋아하는 친구의 주변 탐색, 비어있다면 want2seat 리스트에 추가
    want2seat = set()
    for fr in like[I]:
        if fr in dictt.keys():
            x,y = dictt[fr]
            for dx,dy in d:
                nx,ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and not seat[nx][ny]:
                    want2seat.add((nx,ny))
    if not want2seat:
        for i in range(N):
            for j in range(N):
                if seat[i][j] == 0:
                    want2seat.add((i,j))
    want2seat = list(want2seat)
    where2seat = []
    while want2seat:
        x,y = want2seat.pop()
        F,B = 0,0
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] == 0:
                    B += 1
                elif seat[nx][ny] in like[I]:
                    F += 1
            where2seat.append((4-F,4-B,x,y))
    f,b,i,j = sorted(where2seat)[0]
    seat[i][j] = I
    dictt[I] = (i,j)
    return

def satisfying():
    satisfaction = 0
    # 학생 수 만큼 반복문
    for i in range(1,N*N+1):
        x,y = dictt[i]
        friend = 0
        # i번째 학생 주위를 탐색, 좋아하는 친구가 상하좌우에 존재하면 만족하는 것
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in like[i]:
                    friend += 1
        if friend > 0: 
            satisfaction += 10**(friend-1)
    return satisfaction

N = int(input())
# like[i] : i번째 학생이 좋아하는 친구들 리스트
like = {}
# 학생들의 자리배치 현황표, dictt에는 i번째 친구가 앉은 좌표를 저장
seat = [[0]*N for _ in range(N)]
dictt = {}
d = [(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(N*N):
    arr = list(map(int,input().split()))
    I = arr[0]
    like[I] = arr[1:]
    where(I)
print(satisfying())