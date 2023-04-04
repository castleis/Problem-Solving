N,M = map(int,input().split())
mapp = list(input().split() for _ in range(N))
direction = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}