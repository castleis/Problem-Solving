# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력. 대소문자 구분을 하지 않으며 구두점 또한 무시
'''
입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
출력
"ball"
'''

paragraph = input().lower().split()
new_para = []
for word in paragraph:
    new = ''
    for i in word:
        if i not in '",.':
            new += i       
    new_para.append(new)

banned = input()
words = set(new_para)
dict = {}
for word in words:
    dict[word] = 0

for word in new_para:
    if word == banned:
        continue
    else:
        dict[word] += 1
# dictionary 밸류 값을 기준으로 최댓값 구하기
# 
maxx = 0
for i in range(len(dict)):
    if dict[i] > maxx:
        result = i
print(result)

# Sol1. 리스트 컴프리헨션, Counter 객체 이용
import collections
def mostCommonWord(paragraph,banned):
    # 데이터 클렌징, 정규식으로 표현
    # 단어 문자가 아닌 모든 문자('[^\w]')를 공백(' ')으로 치환
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    # 이 문제에서 most_common(1)은 [('ball', 2)]가 됨.
    return counts.most_common(1)[0][0]