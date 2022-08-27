import sys
sys.stdin = open('0816\\1974.txt')

T = int(input())
for t in range(1,T+1):
    gogo = sum(range(1,10))
    errorr = 0
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int,input().split())))

    for i in range(9):
        if sum(sudoku[i]) != gogo:
            errorr += 1

        sum_col = 0
        for j in range(9):
            sum_col += sudoku[j][i]
        if sum_col != gogo:
            errorr += 1

        sum_box = 0
        for x in range(3):
            for y in range(3):
                sum_box += sudoku[3*(i%3)+x][3*(i%3)+y]
        if sum_box != gogo:
            errorr += 1
    
    if errorr == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
    
