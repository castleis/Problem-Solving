for _ in range(int(input())):
    orders = list(input())
    t_x, t_y = 0, 0
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    for order in orders:
        if order == 'F':
            t_y