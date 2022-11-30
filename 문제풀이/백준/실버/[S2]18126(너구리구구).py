'''
존나 어썸포테이토 코드
'''
N = int(input())
info = [[] for _ in range(N+1)]
for _ in range(N-1):
    room1, room2, distance = map(int,input().split())
    info[room1].append((room2, distance))
    info[room2].append((room1, distance))
maxx = 0
visited = [0]*(N+1)
visited[1] = 1
for r,d in info[1]:
    stack = [(r,d)]
    visited[r] = d
    while stack:
        room, distance = stack.pop()
        # print(f' ============== {room} ============== ')
        # print(f'visited : {visited}')
        flag = True
        # print(info[room])
        for R, D in info[room]:
            if not visited[R]:
                visited[R] = visited[room] + D
                stack.append((R,D))
                flag = False

        if flag:
            # print(visited[room], maxx)
            maxx = max(visited[room], maxx)
            # print(f'ans : {maxx}')
print(maxx)
'''
4
1 2 2
1 3 3
1 4 4

6
1 2 1
2 3 2
2 4 4
3 5 5
2 6 1
'''