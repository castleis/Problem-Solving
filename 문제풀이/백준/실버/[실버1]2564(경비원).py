import sys
input = sys.stdin.readline

w,h = map(int,input().split())
n = int(input())
shops = []
for _ in range(n):
    shops.append(list(map(int, input().split())))
dg = list(map(int,input().split()))

sums = 0
for x in range(n) : 
    i,j = shops[x]
    if dg[0] == i:
        sums += abs(dg[1] - j)
    else:
        # 동근이가 북쪽(1)일 때
        if dg[0] == 1:
            if i == 3:
                sums += dg[1] + j
            elif i == 4 :
                sums += (w - dg[1]) + j
            else:
                sum_1 = h + dg[1] + j
                sum_2 = h + 2*w -(dg[1] + j)
                sums += min(sum_1,sum_2)
        # 동근이가 남쪽(2)일 때
        elif dg[0] == 2 :
            if i== 3:
                sums += dg[1] +(h - j)
            elif i == 4 :
                sums += (w - dg[1]) + (h - j)
            else:
                sum_1 = h + dg[1] + j
                sum_2 = h + 2*w -(dg[1] + j)
                sums += min(sum_1,sum_2)
        # 동근이가 서쪽(3)일 때
        elif dg[0] == 3 :
            if i == 1:
                sums += dg[1] + j
            elif i == 2 :
                sums += (h - dg[1]) + j
            else :
                sum_1 = w + dg[1] + j
                sum_2 = w + 2*h - (dg[1] + j)
                sums += min(sum_1, sum_2)
        # 동근이가 동쪽(4)일 때
        else:
            if i == 1 :
                sums += dg[1] + (w - j)
            elif i == 2 :
                sums += (h - dg[1]) + (w - j)
            else :
                sum_1 = w + dg[1] + j
                sum_2 = w + 2*h - (dg[1] + j)
                sums += min(sum_1, sum_2)
print(sums)