from itertools import combinations as cb
from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ways = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    ways[A].append(B)
    ways[B].append(A)
print(ways)
