

def solve():
    if N == 1 and sum(H) == B:
        return 0
        
    s,e = 0,0
    sums = 0
    ans = []
    while s < N and e < N:
        sums += S[e]
        if sums > B:
            ans.append(sums-B)
            sums -= S[s]
            s += 1
        e += 1
    return ans
            
T = int(input())
for t in range(1,T+1):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    S = sorted(H, reverse = True)      
    print(solve())