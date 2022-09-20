
def solve(N):
    result = ''
    for i in range(-1,-14,-1):
        result += str(int(N // (2**i)))
        N %= 2**i
        if N == 0:
            return result
    return 'overflow'

T = int(input())
for t in range(1,T+1):
    N = float(input())
    print(f'#{t} {solve(N)}')
