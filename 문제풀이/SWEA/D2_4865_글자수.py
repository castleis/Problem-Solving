import sys
sys.stdin = open('0816\\4865.txt')

T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    string = {}
    for s in str1:
        if s not in string:
            string[s] = 0
    for i in string:
        for j in str2:
            if i == j:
                string[i] += 1
    maxx = 0
    for s in string:
        if maxx < string[s]:
            maxx = string[s]
    print(f'#{t} {maxx}')
