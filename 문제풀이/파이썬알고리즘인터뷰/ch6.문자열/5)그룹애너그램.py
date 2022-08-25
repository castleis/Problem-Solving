# 문자열 배열을 받아 애너그램 단위로 그룹핑하기
'''
eat tea tan ate nat bat
'''
arr = input().split()
setword = []
for word in arr:
    if set(word) not in setword:
        setword.append(set(word))

result = [[] for _ in range(len(setword))]
print(result)
for word in arr:
    for i in range(len(setword)):
        if set(word) == setword[i]:
            result[i].append(word)
print(result)


# Sol1. 정렬하여 딕셔너리에 추가
'''
애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖는다.
정렬한 값을 키로 하여 딕셔너리에 추가
존재하지 않는 키를 삽입하려 할 경우 KeyError가 발생하므로 항상 디폴트를 생성해주는 defaultdict()로 선언.
   -> 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간결하게 구성
'''
import collections

def groupAnagrams(strs):
    # 딕셔너리 선언
    anagrams = collections.defaultdict()

    for word in strs:
        # 각 애너그램 그룹의 key : ''.join(sorted(word))
        anagrams[''.join(sorted(word))].append(word)
    # 딕셔너리의 value들만 리스트로 return
    return list(anagrams.values())