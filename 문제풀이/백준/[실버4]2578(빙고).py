import itertools
board, a = [], []

for _ in range(5):
    board.append(list(map(int,input().split())))
for _ in range(5):
    a.append(list(map(int,input().split())))
b = list(itertools.chain(*a))

# b의 숫자를 board에 해당하는 인덱스를 통해 check 리스트에 +1 해줌. 5가 되면 가로 or 세로 줄이 모두 체크 되었다는 뜻
check  = [[0]*5 for _ in range(2)]
check.append(0)
check.append(0)

cnt = 0
bingo = 0

for i in b:
    cnt += 1
    # board의 각 행에 대해서
    for j in range(5):
        # i 가 board[j] 행에 있다면 c에 해당 인덱스를 저장합니다.
        if i in board[j]:
            c = board[j].index(i)
            print(f'i,j,c,cnt : {i},  {j},{c},{cnt}')
            # check리스트의 가로 빙고 칸에 +1 
            # 이하의 모든 if 문은 bingo 갯수를 파악하기 위함.
            check[0][j] += 1
            if check[0][j] == 5:
                bingo += 1
                check[0][j] == 0

            # 세로 빙고 칸에도 +1
            check[1][c] += 1
            if check[1][c] == 5:
                bingo += 1
                check[1][c] == 0

            # 대각선 빙고를 체크
            if j == c:
                check[-2] += 1
                if check[-2] == 5:
                    bingo += 1

            # 반대 대각선 빙고를 체크
            if c == (4 - j):
                check[-1] += 1
                if check[-1] == 5:
                    bingo += 1
            print(cnt,check)
        
            print(f'bingo : {bingo}')
    # 빙고가 된 줄이 3개 이상이라면 지금까지 시행횟수를 출력하고 break
    if bingo >= 3:
        print(cnt)
        break
        
