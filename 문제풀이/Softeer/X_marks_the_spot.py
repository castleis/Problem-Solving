import sys

N = int(sys.stdin.readline())
answer = []

for _ in range(N):
    Si, Ti = sys.stdin.readline().split()

    for i in range(len(Si)):
        if Si[i] == 'x' or Si[i] == 'X':
            idx_X = i
            break

    answer.append(Ti[idx_X].upper())
answer = ''.join(answer)
print(answer)
