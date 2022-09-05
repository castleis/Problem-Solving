# 리트코드 20

def isValid(s):
        dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            else:
                if dict[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
        print(stack)
        if not stack:
            return 'true'
        else:
            return 'false'

s = '(]'
print(isValid(s))