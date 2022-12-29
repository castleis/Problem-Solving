import sys
input = sys.stdin.readline
def combi(n,r,s):
    if r == 6:
        print(*cb)
    else:
        for i in range(s, n+r-5):
            cb[r] = nums[i]
            combi(n, r+1, i+1)

while 1:
    k, *nums = map(int,input().split())
    if k == 0:
        break
    cb = [0]*6
    combi(len(nums),0,0)
    print()
