import sys
input = sys.stdin.readline

def search(trees,M):
    start = 0
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2
        tree = 0
        for t in trees:
            if t > mid :
                tree += t-mid

        if tree < M :
            end = mid-1
        else:
            ans = mid         
            start = mid + 1 
    return ans
        
N,M = map(int,input().split())
trees = list(map(int,input().split()))
ans = search(trees,M)
print(ans)