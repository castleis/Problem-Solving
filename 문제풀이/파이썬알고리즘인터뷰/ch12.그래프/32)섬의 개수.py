# leetcode 200
def numIslands(grid):
    islands = []
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '1':
                islands.append((i,j))
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    ans = 0
    print(islands)
    while islands:
        stack = [islands.pop(0)]
        grid[stack[0][0]][stack[0][1]] = '0'
        while stack:
            x,y = stack.pop()
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == '1':
                        islands.remove((nx,ny))
                        stack.append((nx,ny))
                        grid[nx][ny] = '0'

        print(islands)
        ans += 1
    return ans
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))

# Solution
'''
dfs로 그래프 탐색!
'''
def numIslands1(grid):
    # 이렇게 함수 내에 함수를 사용하면(중첩 함수) numIslands1 함수 내에서만 dfs 함수 호출이 가능한 제약이 생김.
    # 하지만 중첩 함수는 부모 함수에서 선언한 변수도 유효한 범위 내에서 사용 가능!
    def dfs(i,j):
        # 더 이상 땅이 아닌 경우에 종료
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i,j)
                count += 1
    return count
    