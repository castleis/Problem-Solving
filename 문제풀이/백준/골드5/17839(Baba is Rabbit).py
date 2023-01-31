from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(word):
    visited[word] = True
    for w in mapp[word]:
        if not visited[w]:
            ans.add(w)
            dfs(w)

N = int(input())
mapp = defaultdict(list)
for _ in range(N):
    p, iss, q = input().split()
    mapp[p].append(q)

ans = set()
for word in mapp['Baba']:
    visited = defaultdict(dict)
    ans.add(word)
    dfs(word)

answer = sorted(list(ans))
# for a in answer:
#     print(a)
print('\n'.join(sorted(list(ans))))