import sys
sys.stdin = open('1952.txt')
# 고집을 버리고... 세달 권을 n번씩 뽑아가면서(?) 가지치기도 하면서 최솟값을 구하기???

def solve(m,s):
    if m == 12:
        result.append(s)
        return
    if m > 12:
        return
    solve(m+1, s+pay[m])
    solve(m+3, s+c)

T = int(input())
for t in range(1,T+1):
    a,b,c,d = map(int,input().split())
    arr = list(map(int,input().split()))
    pay = [0]*12
    for i in range(12):
        pay[i] = min(arr[i]*a, b)
    result = [d]
    solve(0,0)
    print(f'#{t} {min(result)}')
