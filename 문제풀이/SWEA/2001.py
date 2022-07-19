T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        
    sums = []
    for x in range(N-M+1):
        for y in range(N-M+1):
            flies = 0
            for i in range(M):
                for j in range(M):
                    flies += board[x+i][y+j]
            sums.append(flies)
    print(len(sums))
    answer = max(sums)
    print(f'#{t} {answer}')
#마지막 answer 구할 때, flies를 sums 리스트에 저장하지 말고, max_flies = 0이라는 변수를 만들어 놓고, flies와 비교하여 최댓값만을 저장해놓으면
#메모리 사용(?)이 줄어들지 않을까
#밑의 코드는 해당 내용의 솔루션이다. (8줄부터 시작)
    max_flies = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
          flies = 0
          for i in range(M):
            for j in range(M):
              flies += board[x+i][y+j]
          if flies > max_flies:
            max_flies = flies
    print(f'#{t} {max_flies}')
