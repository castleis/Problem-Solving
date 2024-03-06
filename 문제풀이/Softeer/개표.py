T = int(input())
for t in range(T):
    n = int(input())
    plus = int(n // 5)
    bar = int(n % 5)

    result = []
    for cnt in range(plus):
        result.append('++++')
    result.append('|'*bar)

    answer = ' '.join(result)
    print(answer)
    
