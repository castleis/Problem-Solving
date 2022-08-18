N,L,R = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

d = [[1,0],[-1,0],[0,1],[0,-1]]

def startpoint(arr):
    for x in range(N):
        for y in range(N):
            for i,j in d:
                if 0 <= x+i < N and 0 <= y+j < N:
                    if L <= abs(arr[x][y] - arr[x+i][y+j]) <= R :
                        return x,y

visited = [[0]*(N) for _ in range(N)]
def united_country(day):
    print(f'================{day}일째=====================')
    # 스택 만들기
    if day == 1:
        stack = startpoint(arr)
        if stack == None:
            return 0

    for i in visited:
        if i == day-1:
            stack.append(i)
    print(f'시작 스택 : {stack}')
    print(visited)

    unite = []
    population = 0
    # 탐색 시작
    while stack:
        x,y = stack.pop()
        for i,j in d:
            # print(f'[{x},{y}]')
            if 0 <= x+i < N and 0 <= y+j < N:
                if visited[x+i][y+j] < day:
                    # print(f'인구수 차이 {abs(arr[x][y] - arr[x+dx[i]][y+dy[i]])}')
                    if L <= abs(arr[x][y] - arr[x+i][y+j]) <= R :
                        visited[x+i][y+j] = day
                        stack.append((x+i, y+j))
                        unite.append((x+i, y+j))
                        population += arr[x][y]
                        # print(f'visited : {visited}')
    return unite,population


def migrate(arr):
    day = 1
    while True:
        country,population = united_country(day)
        print(f'{day}일째 연합국가 : {country}')

        if len(country) == 0:
            print(f"didn't move : {arr}")
            return day-1

        mean = population // len(country)
        print(f'mean : {mean}')
        for i,j in country:
            arr[i][j] = mean
        day += 1

ans = migrate(arr)
print(f'정답 : {ans}')