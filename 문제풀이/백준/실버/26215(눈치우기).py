N = int(input())
snows = list(map(int,input().split()))
# print('snows :', snows)
days = 0
if N > 1:
    while snows[-1] > 0:
        
        snows[-1] -= 1
        snows[-2] -= 1
        days += 1
        snows.sort()
else:
    days += snows[0]

print(days if days <= 1440 else -1)

n = int(input())
snow = list((map(int, input().split())))
res = 0
m = max(snow)
s = sum(snow)

if m > 1440:
    print(-1)
elif m >= s-m:
    print(m)
else:
    res = (m + (s-2*m)//2 + (s-2*m) %2)
    if res > 1440:
        print(-1)
    else:
        print(res)