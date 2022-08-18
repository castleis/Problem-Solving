import sys
sys.stdin = open('0818\\4866.txt')

T = int(input())
for t in range(1,T+1):
    a = str(input())
    stack = []
    for i in a:
        if i == '(' or i == '{':
            stack.append(i)
            print(stack)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
                print(stack)
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
                print(stack)
        else:
            continue
    if stack :
        print(f'#{t} 0')
    else:
        print(f'#{t} 1')