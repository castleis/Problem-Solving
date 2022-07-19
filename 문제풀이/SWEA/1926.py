N = int(input())
num = []
for i in range(1, N+1):
    num.append(i)

num = list(map(str, num))
result = []
for i in num:
    cnt = 0
    cnt += i.count('3')
    cnt += i.count('6')
    cnt += i.count('9')
    if cnt == 0:
        result.append(i)
    else :
        result.append('-'*cnt)
print(' '.join(result))
