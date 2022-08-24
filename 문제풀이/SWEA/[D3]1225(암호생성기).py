import sys
sys.stdin = open('SWEA/input/1225.txt')

while True:
    try:
        t = int(input())
        arr = list(map(int,input().split()))
        front = rear = -1
        Create = True
        while Create:
            for i in range(1,6):
                num = arr.pop(0)
                if num-i > 0:
                    arr.append(num-i)
                elif num - i <= 0:
                    arr.append(0)
                    Create = False
                    break
        print(f'#{t}', end = ' ')
        print(*arr)
    except:
        break
            
'''
#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0 

'''