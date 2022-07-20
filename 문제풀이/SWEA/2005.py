T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []

    #피라미드 모양의 board 생성
    for i in range(N):
        board.append([0]*(i+1))
        board[i][0], board[i][i] = 1 ,1  #첫번째와 맨 끝 값은 1 고정

    # 2차원 배열에서 두번째 줄의 숫자는 
    # 자신의 윗줄의 왼쪽과 오른쪽 숫자의 합으로 나타낼 수 있음
    for k in range(1,N-1):
        for j in range(1,k+1):
            board[k+1][j] = board[k][j-1] + board[k][j]

    # 2차원 배열을 출력 형태에 맞게 출력.. 이 어렵네
    print(f'#{t}')
    for c in range(N):
        for d in range(c+1):
            print(board[c][d], end = ' ')
        print()  #이거 하나때문에... 고민에 고민을 ㅠㅠ

