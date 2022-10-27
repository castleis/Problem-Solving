'''
import sys
input = sys.stdin.readline
N = int(input())
Nums = {}
A = list(map(int,input().split()))
for a in A:
    Nums[a] = 1
M = int(input())
X = list(map(int,input().split()))

for x in X:
    try:
        if Nums[x]:
            print(1)
        else:
            print(0)
    except:
        print(0)
'''
ip = input
def main():
    ip()
    n = ip().strip().split(' ')
    print(n)
    ip()
    
    s = set(n)
    r = ''
    for k in input().strip().split(' '):
        r += '1\n' if k in s else '0\n'
        print(r)
    print(r)

if __name__ == "__main__":
    main()