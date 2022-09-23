'''
5
123123
124467
333444
444456
123444
'''
def f(i,k):
    global ans
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] == card[2]:
            tri += 1
        if card[0]+1 == card[1] and card[1]+1 == card[2]:
            run += 1
        if card[3] == card[4] == card[5]:
            tri += 1
        if card[3]+1 == card[4] and card[4]+1 == card[5]:
            run += 1
        if tri+run == 2:
            ans = 'Baby Gin'
    else:
        for j in range(i,k):
            card[i],card[j] = card[j], card[i]
            f(i+1,k)
            card[i], card[j] = card[j], card[i]

T = int(input())
for t in range(1,T+1):
    card = list(map(int,input()))
    ans = 'Lose'
    f(0,6)
    print(f'#{t} {ans}')
# ===============================
T = int(input())
for t in range(1,T+1):
    card = int(input())
    c = [0]*12  # 같은 코드로 run, tri를 확인하기 위해서 뒤에 두칸을 더 붙여놓은 것! (인덱스 10,11 자리)

    # 이건 뭘... 하려구? @.@??
    i = 0
    while i < 6:
        c[card%10] += 1
        card //= 10
        i += 1

    # run, triplet 검사
    tri, run = 0,0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run+tri == 2:
        print(f'#{t} Baby Gin')
    else:
        print(f'#{t} Lose')