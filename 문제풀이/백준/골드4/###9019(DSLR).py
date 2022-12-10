# Pypy에서 틀림... ㅜㅡㅜ 고치기
import sys
input = sys.stdin.readline
from collections import deque
def cal(A,B):
    visited = ['']*10001
    queue = deque()
    queue.append(A)
    while queue:
        num = queue.popleft()
 
        D = (2*num)%10000
        if D == B:
            return visited[num]+'D'
        if not visited[D]:
            queue.append(D)
            visited[D] = visited[num] + 'D'

        S = num-1 if num > 0 else 9999
        if S == B:
            return visited[num]+'S'
        if not visited[S]:
            queue.append(S)
            visited[S] = visited[num] + 'S'

        L = (num%1000)*10 + num//1000
        if L == B:
            return visited[num]+'L'
        if not visited[L]:
            queue.append(L)
            visited[L] = visited[num] + 'L'

        R = (num%10)*1000 + num//10
        if R == B:
            return visited[num]+'R'
        if not visited[R]:
            queue.append(R)
            visited[R] = visited[num] + 'R'

        # print(f'{num} : {D},{S},{L},{R}')


T = int(input())
for t in range(T):
    A,B = map(int,input().split())
    print(cal(A,B))