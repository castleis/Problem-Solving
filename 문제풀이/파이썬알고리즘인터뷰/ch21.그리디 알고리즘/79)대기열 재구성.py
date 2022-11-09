# leetcode 406
from collections import deque
class Solution:
    def reconstructQueue(self, people):
        '''
        [h,k]
        [키, 본인 앞에... 같거나 큰 사람이 몇명 있는지]
        -> k에 맞는 순서를 가지도록 재구성하기
        '''
        people.sort()
        print(people)
        # for i in range(len(people)):
        #     for j in range(i,len(people)):
        #         # 순위를 비교해서 자기(i)보다 작거나 같다!
        #         if people[i][1] >= people[j][1]:
        #             # 근데 심지어 키까지 작다!
        #             if people[i][0] > people[j][0]:
        #                 # 내가 뒤로 ㅜㅜ 똑가태...
        #                 people[i], people[j] = people[j], people[i]
        # print(people)

a = Solution()
a.reconstructQueue(people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])