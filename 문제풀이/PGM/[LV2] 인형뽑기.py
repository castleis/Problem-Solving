def solution(board, moves):
    N = len(board)
    ans = 0
    B = [0]
    for j in moves:
        for i in range(N):
            if board[i][j-1] != 0:
                if B[-1] == board[i][j-1]:
                    B.pop()
                    ans += 2
                else:
                    B.append(board[i][j-1])
                board[i][j-1] = 0
                break
    return ans

board, moves = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]
print(solution(board, moves))

# 1 5 3 5 1 2 1 4
# 4 3 1 1 3 2 0 4