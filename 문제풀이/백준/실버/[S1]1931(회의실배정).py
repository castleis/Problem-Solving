import sys
input = sys.stdin.readline

N = int(input())
meeting = [tuple(map(int,input().split())) for _ in range(N)]
meeting.sort(key = lambda x : (x[1],x[0]))
S,E = meeting[0]
cnt = 1
for i in range(1,N):
    if E <= meeting[i][0]:
        cnt += 1
        S,E = meeting[i]
print(cnt)