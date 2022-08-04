import sys

n,k = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

max_s = 0
s = 0
for i in range(k):
    s += a[i]
    max_s = s

for j in range(0,len(a)-k):
    s = s - a[j] + a[j+k]
    if max_s < s:
        max_s = s  
print(max_s)

# Solution
def solve(n,k,arr):
    temp = sum(arr[:k])
    ans = temp

    for i in range(k,n):
        temp += arr[i]
        temp -= arr[i-k]
        if temp > ans:
            ans = temp
    return ans if n!=k else temp
if __name__ == '__main__':
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n,k,arr))