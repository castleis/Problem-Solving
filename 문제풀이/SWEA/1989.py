N = int(input())
case_num = 0
for _ in range(N):
    case_num += 1
    word = list(input().strip())
    word_set = set(word)
    if len(word)%2 == 0:
        if len(word)/2 == len(word_set):
            print(f'#{case_num} 1')
        else:
            print(f'#{case_num} 0')
    else:
        if (len(word)//2)+1 == len(word_set):
            print(f'#{case_num} 1')
        else:
            print(f'#{case_num} 0')