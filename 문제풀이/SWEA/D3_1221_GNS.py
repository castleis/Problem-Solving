import sys
sys.stdin = open('0812\\1221.txt')

# 버블정렬 너무 오래걸린다!
# def translate(arr):
#     num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
#     for i in range(n):
#         for j in range(i+1,n):
#             if num[arr[i]] > num[arr[j]] :
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr

def translate(arr):
    num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    if len(arr) <= 1:
        return arr
    s,e,b = [], [],[]
    pivot = len(arr)//2
    for i in range(len(arr)):
        if num[arr[i]] > num[arr[pivot]] :
            b.append(arr[i])
        elif num[arr[i]] < num[arr[pivot]] :
            s.append(arr[i])
        else :
            e.append(arr[i])
    return translate(s)+e+translate(b)


T = int(input())
for _ in range(T):
    t, n = input().split()
    n = int(n)
    arr = list(input().split())
    ans = ' '.join(translate(arr))
    print(t)
    print(ans)


