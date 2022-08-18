import sys
sys.stdin = open('0818\\1234.txt')

for _ in range(10):
    n,arr = input().split()
    arr = list(map(str, arr))
    print(arr)