import sys
sys.stdin = open('0816\\4865.txt')

# 외않되? @ㅠ@ ?????????????????? 됨;;
def find(pattern,target):
    M = len(pattern)
    N = len(target)

    for i in range(N-M+1):
        if target[i:i+M] == pattern:
            return 1
    return 0

T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    ans = find(str1,str2)
    print(f'#{t} {ans}')