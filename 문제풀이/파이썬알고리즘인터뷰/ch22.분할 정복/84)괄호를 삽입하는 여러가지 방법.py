# leetcode 241
class Solution:
    def diffWaysToCompute(self, expression: str):
        ans = []
        def divideAndConquer(i,expression):
            # 정복 : 숫자만이면 int로 리턴하기
            if len(expression) == 1:
                return int(expression)
            if 2*(i+1) > len(expression):
                expression1 = expression[0]
                operator = expression[1]
                expression2 = expression[2]
            # 조합 및 분할
            else:
                expression1 = expression[:2*i+1]
                expression2 = expression[2*(i+1):]
                operator = expression[2*i+1]
            print(f'ex1 : {expression1}')
            print(f'oper : {operator}')
            print(f'ex2 : {expression2}')
            if operator == '+':
                return divideAndConquer(i+1,expression1) + divideAndConquer(i+1,expression2)
            elif operator == '-':
                return divideAndConquer(i+1,expression1) - divideAndConquer(i+1,expression2)
            elif operator == '*':
                return divideAndConquer(i+1,expression1) * divideAndConquer(i+1,expression2)

        i = 0
        while 2*(i+1) <= len(expression):
            print(f'================ {i} : {2*i+1}, {2*(i+1)}, {expression} =================')
            ans.append(divideAndConquer(i,expression))
            i += 1
            print(ans)
        return ans
a = Solution()
# expression = "2-1-1"
expression = "2*3-4*5"
print(a.diffWaysToCompute(expression))

# Solution
def diffWaysToCompute1(expression):
    def calculate(left,right,op):
        print(left, op, right)
        sub_results = []
        for L in left:
            for R in right:
                print(f'L : {L}, R : {R}')
                sub_results.append(eval(str(L) + op + str(R)))
                print(f'sub : {sub_results}')
        return sub_results
    
    def divideAndConquer(expression):
        if expression.isdigit():
            return [int(expression)]
        results = []
        for index, value in enumerate(expression):     
            if value in '+-*':
                print(f'============= val : {value},({index}) {expression} =============')
                left = divideAndConquer(expression[:index])
                right = divideAndConquer(expression[index+1:])
                results.extend(calculate(left, right, value))
                print(f'==== results : {results} / L : {left}, R : {right} ====')
        return results
    return divideAndConquer(expression)
'''
============= val : *,(1) 2*3-4*5 =============
    ============= val : -,(1) 3-4*5 =============
        ============= val : *,(1) 4*5 =============
        [4] * [5]
        L : 4, R : 5
        sub : [20]
        ==== results : [20] ====
    [3] - [20]
    L : 3, R : 20
    sub : [-17]
    ==== results : [-17] ====
    ============= val : *,(3) 3-4*5 =============
        ============= val : -,(1) 3-4 =============
        [3] - [4]
        L : 3, R : 4
        sub : [-1]
        ==== results : [-1] ====
    [-1] * [5]
    L : -1, R : 5
    sub : [-5]
    ==== results : [-17, -5] ====
[2] * [-17, -5]
L : 2, R : -17
sub : [-34]
L : 2, R : -5
sub : [-34, -10]
==== results : [-34, -10] ====
============= val : -,(3) 2*3-4*5 =============
    ============= val : *,(1) 2*3 =============
    [2] * [3]
    L : 2, R : 3
    sub : [6]
    ==== results : [6] ====
    ============= val : *,(1) 4*5 =============
    [4] * [5]
    L : 4, R : 5
    sub : [20]
    ==== results : [20] ====
[6] - [20]
L : 6, R : 20
sub : [-14]
==== results : [-34, -10, -14] ====
============= val : *,(5) 2*3-4*5 =============
    ============= val : *,(1) 2*3-4 =============
        ============= val : -,(1) 3-4 =============
        [3] - [4]
        L : 3, R : 4
        sub : [-1]
        ==== results : [-1] / L : [3], R : [4]====
    [2] * [-1]
    L : 2, R : -1
    sub : [-2]
    ==== results : [-2] ====
    ============= val : -,(3) 2*3-4 =============
        ============= val : *,(1) 2*3 =============
        [2] * [3]
        L : 2, R : 3
        sub : [6]
        ==== results : [6] ====
    [6] - [4]
    L : 6, R : 4
    sub : [2]
    ==== results : [-2, 2] ====
[-2, 2] * [5]
L : -2, R : 5
sub : [-10]
L : 2, R : 5
sub : [-10, 10]
==== results : [-34, -10, -14, -10, 10] ====

'''