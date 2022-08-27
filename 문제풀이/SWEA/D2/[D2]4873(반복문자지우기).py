import sys
sys.stdin = open('0818\\4873.txt')

def repeat(string):
    if len(string) == 1:
        return string

    elif len(string) == 0:
        return 0
    else:
        stack = [string[0]]
        for i in range(1,len(string)):
            if string[i] == stack[-1]:
                string.pop(i)
                string.pop(i-1)
                return repeat(string)
            else:
                stack.append(string[i])
        return string

T = int(input())
for t in range(1,T+1):
    s = list(input())
    ans = repeat(s)
    print(f'#{t} {len(ans)}')


    
