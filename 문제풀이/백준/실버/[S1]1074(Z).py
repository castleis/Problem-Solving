def solve(x,y,N,cnt):
    # print(f'=============== {N} [{x},{y}]: {cnt}==============')
    if N == 1:
        if x == r and y == c:
            print(cnt)
            quit()
        # if x == r and y+1 == c:
        #     print(cnt+1)
        #     quit()
        # if x+1 == r and y == c:
        #     print(cnt+2)
        #     quit()
        # if x+1 == r and y+1 == c:
        #     print(cnt+3)
        #     quit()
    n = N//2
    if x <= r < x+n and y <= c < y+n:
        solve(x,y,n,cnt)
    if x <= r < x+n and y+n <= c <= y+2*n:
        solve(x,y+n,n, cnt+n*n)
    if x+n <= r <= x+2*n and y <= c < y+n:
        solve(x+n,y,n, cnt+2*n*n)
    if x+n <= r <= x+2*n and y+n <= c <= y+2*n:
        solve(x+n,y+n,n, cnt+3*n*n)

N,r,c = map(int,input().split())
solve(0,0,2**N,0)