# leetcode 371

def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    bin_a = bin(a & MASK)[2:].zfill(32)
    bin_b = bin(b & MASK)[2:].zfill(32)
    num = ''
    flag = False
    for i in range(31,-1,-1):
        if bin_a[i] and bin_b[i]:
            if flag:
                num = '1'+num
            else:
                num = '0'+num
            flag = True
            
        elif bin_a[i] or bin_b[i]:
            if flag:
                num = '0'+num
                flag = True
            else:
                num = '1'+num
                flag = False
        else:
            if flag:
                num = '1' + num
            else:
                num = '0' + num
    print(int(num,2))
    
        

a = 2
b = 3
getSum(a,b)