import sys
input = sys.stdin.readline
N = int(input())
property = list(map(int,input().split()))
property.sort(key=lambda x:abs(x))
resolve = []
x1, x2 = None,None
about_zero = 2000000000
for i in range(N-1):
    val = abs(property[i] + property[i+1])
    if val <= abs(about_zero):
        about_zero = val
        x1 = property[i]
        x2 = property[i+1]
print(min(x1,x2), end=' ')
print(max(x1,x2))

'''
def boj_2470():
    n, values = int(input()), list(sorted(map(int, input().split()), key=abs))
    a, b = values.pop(0), values[0]
    m = abs(a + b)
    for a_, b_ in zip(values, values[1:]):      # 양 옆 요소들을 예쁘게 가져올 수 있꾸나...
        print(f'================================================================')
        print(values)
        print(values[1:])
        print(f'a_ : {a_}, b_ : {b_}')
        m_ = abs(a_ + b_)
        if m_ < m:
            m, a, b = m_, a_, b_
        if m <= 1:
            break
    print(f'{min(a, b)} {max(a, b)}')

def main():
    boj_2470()

if __name__ == '__main__':
    main()
'''

'''
3
-10 1 2
# 1 2

6
1 2 3 4 5 6
# 1 2

5
-101 -3 -1 5 93
# -3 5
'''