T = int(input())
for t in range(1,T+1):
    row = input()
    for i in range(1,len(row)):
        if row[:i] == row[i:2*i]:
            answer = len(row[:i])
            print(f'#{t} {answer}')
            break
