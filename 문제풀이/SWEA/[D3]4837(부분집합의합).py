import sys
sys.stdin = open('0811/4837.txt')

T = int(input())
for t in range(1,T+1):
    arr = [i for i in range(1,13)]
    n,k = map(int,input().split())
    sett = [[]]
    sums = []
    for a in arr:
        size = len(sett)
        for i in range(size):

            sett.append(sett[i]+[a])
        if sum(sett[i]) == k:
            if len(sett[i]) == n:
                print(sett[i])
                sums.append(sum(sett[i]))

    print(sett)

    if sums :
        print(f'#{t} {len(sums)}')
    else:
        print(f'#{t} 0')