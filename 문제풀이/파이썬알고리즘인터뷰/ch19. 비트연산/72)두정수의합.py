# leetcode 371

def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    bin_a = bin(a & MASK)[2:]
    bin_b = bin(b & MASK)[2:]
    
        

a = 2
b = 3
getSum(a,b)