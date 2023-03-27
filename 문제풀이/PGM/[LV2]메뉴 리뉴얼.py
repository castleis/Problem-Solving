from itertools import combinations as cb
from collections import defaultdict
def solution(orders, course):
    courses = defaultdict(dict)
    # courses = {2:{2개짜리 코스:1, ...}, 3:{3개짜리 코스:2,...}, 4:{}, ...}
    for order in orders:
        for n in course:
            combis = cb(order, n)
            for comb in combis:
                # comb에서 'WX'와 'XW'는 같은 구성이기 때문에 처리를 해줘야 함.
                comb = ''.join(sorted(list(comb)))
                # courses의 n개짜리 코스인 comb의 value값을 가져와서(없으면 default = 0) 1 더하기
                courses[n][comb] = courses[n].get(comb, 0) + 1
    answer = []
    for n in course:
        course_list = list(courses[n].items())
        print(course_list)
        # 많이 주문된 순서대로 정렬
        course_list.sort(key = lambda x: -x[1])
        max_n = 0    # n개짜리 코스에서 가장 많이 주문된 횟수
        for candidate, n in course_list:
            if n > 1 and n >= max_n:   # 최대 주문 횟수라면 정답 리스트에 넣어주고, max_n을 갱신
                answer.append(''.join(candidate))
                max_n = n
            elif n < max_n:     # 주문 횟수가 많은 순으로 정렬했기 때문에 주문 횟수가 더 작은 코스 구성을 만나면 바로 break
                break
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))