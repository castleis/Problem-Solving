'''
85%에서 틀렸다고 한다... 도대체 어떤 테스트 케이스를 통과 못하는지 너무너무너무너무 답답한데!!!
근데 또 자리 배치는 제대로 잘 되는 것 같단말이오...

시간 #1 : 72ms,  #2 : 284ms
메모리 30840KB

문제점은 a 리스트를 만드는데에 있었다.. 정확하게 다음 지점까지 갈 수 있는 거리를 구해줬어야 햇는데
그러지 못햇었다. ㅠㅠㅠㅠㅠㅠ 진짜 너무 생고생쓰..
'''

import sys
import time
startt = time.time()
input = sys.stdin.readline

c,r = map(int,input().split())
k = int(input())

arr = [[0]*r for _ in range(c)]

if c*r < k:
    print(0)

else:
    a = []
    while c > 0 and r > 0:
        a.append(r)
        a.append(c-1)
        c -= 1
        r -= 1

    d = [1,1,-1,-1]
    i,j = 1, 0
    location = 0
    # 1 ================================
    # sums = 0
    # for p in range(len(a)):
    #     idx = p
    #     sums += a[p]
    #     if p%2 == 0:
    #         j += d[location]*a[p]
    #     else:
    #         i += d[location]*a[p]
        
    #     location = (location + 1) % 4
    #     if sums >= k:
    #         break
    # if sums == k :
    #     print(i, j)
    # else:
    #     s = sums-k
    #     idxx = idx % 4
    #     if idxx == 0 or idxx == 2:
    #         j += -d[idxx]*s
    #     else:
    #         i += -d[idxx]*s
    #     print(i, j)
    # ===================================

    # 2 =================================
    stopp = False
    x = 0
    for p in range(len(a)):
        if stopp == True:
            break
        for _ in range(a[p]):
            x += 1
            if p%2 == 0:
                j += d[location]
                arr[i-1][j-1] = x
            else:
                i += d[location]
                arr[i-1][j-1] = x
            # print(f'{x} : {i},{j}')
            if x == k:
                stopp = True
                break
        location = (location + 1) % 4
    print(i, j)
    # ===================================   

