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