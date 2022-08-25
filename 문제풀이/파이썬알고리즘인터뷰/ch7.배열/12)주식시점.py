# 한 번의 거래로 낼 수 있는 최대 이익 산출
'''
입력 : 7 1 5 3 6 4
출력 : 5
'''
arr = list(map(int,input().split()))
minn = max(arr)
maxx = 0
profit = []
for i in range(len(arr)):
    if arr[i] < minn:
        minn = arr[i]
        maxx = 0
    elif arr[i] > maxx:
        maxx = arr[i]
        profit.append(maxx-minn)
print(max(profit))


# Sol1. 브루트 포스로 계산 -> 타임아웃으로 풀리지 않는다... ㅠㅡㅠ
def maxProfit1(prices):
    max_price = 0
    for i,price in enumerate(prices):
        for j in range(i,len(prices)):
            # wow;;;;;;;
            max_price = max(prices[j] - price, max_price)
    return max_price


# Sol2. 저점과 현재 값과의 차이 계산 : 카데인 알고리즘, O(n)
import sys
def maxProfit2(prices):
    profit = 0
    # 초기 최솟값은 시스템의 최댓값으로 정한다! (어떤 값이 들어오든 바로 교체될 수 있도록 하기 위해)
    # 반대로 초기 최댓값은 시스템의 최댓값에 (-)한 값을 할당하자 (-sys.maxsize)
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit, price - min_price)
    return profit