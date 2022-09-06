# leetcode 316
def removeDuplicateLetters(s):
    stack = []
    ans = []

    for i in s:
        if i not in stack:
            stack.append(i)
