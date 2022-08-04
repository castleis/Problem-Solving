import time
import sys
starts = time.time()
N = int(sys.stdin.readline())
if N <= 2:
    print(N)
else:    
    nums = list(map(int, sys.stdin.readline().split()))
    # 인접한 원소들의 차이값을 저장해줄 리스트, 연산 후 원소가 1개 부족해지는 것 유의
    subt = []
    for i in range(len(nums)-1):
        sub = nums[i]-nums[i+1]
        subt.append(sub)
    print(subt)
    result = []
    flags = False
    for i in range(len(subt),2,-1):
        for j in range(len(subt)-i):
            p,n = 0,0
            for k in subt[j:j+i]:
                if k > 0:
                    p += 1
                elif k < 0:
                    n += 1
                else :
                    pass
            if n == 0 or p == 0:
                print(i+1)
                flags = True
                break
            else :
                continue
        if flags:
            break
ends = time.time()
print(ends-starts)