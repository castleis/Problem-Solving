T = int(input())
for t in range(1,T+1):
    k,n,m = input().split()
    s = list(map(int, input().split()))
    k,n,m = int(k), int(n), int(m)

    station = [0]*(n+1)
    station[0] = k
    cnt = 0

    for i in range(1,len(s)):
        if s[i] - s[i-1] > k:
            print(f'#{t}')
            print(0)
            continue

    for i in range(1,n):
        station[i] = station[i-1] -1
        if i in s:
            if n - i < k:
                break
            elif s[s.index(i)+2] - i > k:
                cnt += 1
                station[i] += k
        else :
            continue
    print(station)



