import sys
input = sys.stdin.readline

N,M = map(int,input().split())
H = set(input() for _ in range(N))
S = set(input() for _ in range(M))
A = list(H&S)
A.sort()
print(len(A))
print(A)
for name in A:
    print(name)