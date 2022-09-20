
T = int(input())
dict = {'A' : 10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
for t in range(1,T+1):
    N, s = input().split()
    ans = ''
    for n in s:
        if n in dict:
            n = dict[n]
        n = int(n)
        result = ''
        for i in range(4):
            result = str(n%2) + result
            n //= 2
        ans += result
    print(f'#{t} {ans}')

    