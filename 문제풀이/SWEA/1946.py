T = int(input())
for _ in range(T):
    a = []
    answer = []
    k = 0
    N = int(input())
    for i in range(N):
        a.append(input().split())
        k += int(a[i][1])

        # for j in range(int(a[i][1])):
        #     answer.append(a[i][0])

#Solution
T = int(input())
for t in range(1, T+1):
    N = int(input())
    value =" "
    for i in range(N):
        C,K = input().split()
        K = int(K)
        value += C*K

    print("#{t}")
    for i in range(len(value)):
        if (i+1)%10 == 0:
            print(value[i])
        else:
            print(value[i], end =" ")
    print()
    
    
