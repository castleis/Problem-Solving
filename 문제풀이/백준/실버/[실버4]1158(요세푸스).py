N,K = map(int,input().split())
arr = [x for x in range(1,N+1)]
result = []
i = 0
while arr:
    i = (i + K - 1) % len(arr)
    result.append(str(arr.pop(i)))

print("<", ', '.join(result),">", sep='')