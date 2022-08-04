import sys
input = sys.stdin.readline

w,h = map(int,input().split())
n = int(input())
shops = []
for _ in range(n):
    shops.append(tuple(map(int, input().split())))
dong = tuple(map(int,input().split()))

d = [1,3,2,4,1]

sums = 0
for i in range(n):
    
    
print(sums)





