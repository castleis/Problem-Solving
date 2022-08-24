# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력. 대소문자 구분을 하지 않으며 구두점 또한 무시
'''
입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
출력
"ball"
'''


import collections


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
maxx = 0
for i in range(len(dict)):
    if dict[i] > maxx:
        result = i
print(result)

# Sol
'''정규식과 Counter 객체를 이용'''
def mostCommonWord(paragraph,banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    .lower().split()
    if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]