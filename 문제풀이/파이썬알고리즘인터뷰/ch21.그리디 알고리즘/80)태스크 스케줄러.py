# leetcode 621
# Solution
import collections
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n+1):    # most_common() : 가장 개수가 많은 아이템부터 출력하기
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break
            result += n - sub_count + 1
        return result
'''
Counter 모듈 -> dict로 반환
먼저 우선순위 큐를 사용하여 가장 개수가 많은 아이템부터 하나씩 추출.
이 때, 해당 아이템 전체를 추출하는 것이 아니라 하나만 추출하고, 추출했으므로 빠진 개수를 업데이트 해줘야함.
이렇게 하나만 추출 후, 개수를 업데이터 해주는 일을 Counter 모듈이 처리해줄 수 있다.
6줄에서 counter를 정의하고 12줄에서 most_common() 함수로 가장 개수가 많은 아이템부터 출력한다. (사실상 최대 힙과 같은 역할)
pop()으로 추출하는 것이 아니기 때문에 subtract로 1개씩 개수를 별도로 줄여나가준다.
 -> 이처럼 Counter 모듈은 개수를 줄이는 메소드도 지원학 ㅣ때문에 매우 편리
 -> But, Counter는 0과 음수도 처리해주는데 이 문제에서는 0 이하는 필요 없기 때문에 0 이하일 때는 아예 삭제 (18줄)
'''