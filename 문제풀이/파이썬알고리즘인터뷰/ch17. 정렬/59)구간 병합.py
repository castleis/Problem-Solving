# leetcode 56
# 감자 코드.......
def merge(intervals):
    array = []
    intervals.sort()
    for i in range(len(intervals)):
        array += intervals[i]
    print(array)
    result = []
    s,e = 0,2
    maxx = 0
    while e < len(array):
        if array[e-1] >= array[e]:
            e += 2
            continue
        else:
            print(s,e-1)
            print(min(array[s:e]),max(array[s:e]))
            if max(array[s:e]) < maxx:
                e += 2
                continue
            result.append([min(array[s:e]),max(array[s:e])])
            maxx = max(array[s:e])
            s = e
        e += 2
    print(s)
    if max(array[s:e]) > maxx :
        result.append([array[s],max(array[s:e])])
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals1 = [[1,4],[2,3]]
intervals2 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals3 = [[0,0],[1,2],[5,5],[2,4],[3,3],[5,6],[5,6],[4,6],[0,0],[1,2],[0,2],[4,5]]
print(merge(intervals3))

# Solution
# class Solution1:
#     def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
#         merged = []
#         # i : x[0]을 기준으로 정렬된 intervals 리스트의 요소(type : 리스트)
#         for i in sorted(intervals, key = lambda x : x[0]):
#             if merged and i[0] <= merged[-1][1]:
#                 merged[-1][1] = max(merged[-1][1], i[1])
#             # merged에 아무것도 없거나 현재 시작 값이 merged 마지막의 끝 값보다 크다면 (중첩되지 않는다면)
#             # 현재 페어 i를 merged에 더해준다. 
#             else:
#                 merged += i,
#                 # += i, : 콤마(,) 연산자 -> 중첩 리스트를 만들어주는 역할. += [i]와 동일한 역할
#                 # a = [1], b = [2,3]
#                 # a += b, -> [1, [2, 3]]
#         return merged

a = 'slekfkd'
print(sorted(a))
