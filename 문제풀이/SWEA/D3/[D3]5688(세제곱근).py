
def solve(N):
    print(N**(1/3) == int(N**(1/3)))
    if N**(1/3) == int(N**(1/3)):
        return int(N**(1/3))
    else:
        return -1

T = int(input())
dict = {}
for i in range(1,10**6+1):
    dict[i**3] = i
for t in range(1,T+1):
    N = int(input())
    print(f'#{t} {dict.get(N,-1)}')