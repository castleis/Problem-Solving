# 로그를 재정렬. 
# 기준은 다음과 같다.
'''
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
입력
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
'''
def reorderLogFiles(logs):
    letters,digits = [],[]
    for log in logs:
        print(log.split()[1])
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    print(f'letters, 문자열 로그 : {letters}')
    print(f'digits, 숫자 로그 : {digits}')
    # 식별자를 제외한 문자열[1:]을 키로 하여 정렬하며 동일할 경우 후순위로 식별자[0]을 지정해 정렬되도록 함.
    letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
    return letters + digits
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))