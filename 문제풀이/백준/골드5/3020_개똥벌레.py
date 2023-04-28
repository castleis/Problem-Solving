N,H = map(int,input().split())
# obstacles = [int(input()) for _ in range(N)]
suk, jong = [], []
for n in range(N):
    if n % 2 :
        jong.append(H - int(input()))
    else:
        suk.append(int(input()))
suk.sort()
jong.sort(reverse=True)
mid = (max(suk) + min(suk)) // 2
def breaking(m):
    cnt = 0
    for i in range(N//2):
        if suk[i] >= m:
            cnt += len(suk[i:])
            break
    for j in range(N//2):
        if jong[j] <= m:
            cnt += len(jong[j:])
            break
    return cnt
print(breaking(7))