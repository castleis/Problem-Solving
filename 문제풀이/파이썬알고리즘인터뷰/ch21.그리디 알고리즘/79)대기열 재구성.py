# leetcode 406
from collections import deque
class Solution:
    def reconstructQueue(self, people):
        '''
        [h,k]
        [키, 본인 앞에... 같거나 큰 사람이 몇명 있는지]
        -> k에 맞는 순서를 가지도록 재구성하기
        그리디???????????????????????????????????????????????????????????????????????
        무엇을 그리디 어떠ㅓㅎ계 그리디
        '''
        result = []
        people.sort(key = lambda x : (x[0],-x[1]))
        while people:
            h,k = people.pop()
            if not result:
                result.append([h,k])
                continue
            for i in range(len(result)):
                hi,ki = result[i]
                if h == hi:
                    if k < ki:
                        result.insert(i, [h,k])
                        break
                    else:
                        if i == len(result)-1:
                            result.append([h,k])
                            break
                        else:
                            continue
                elif h <= hi:
                    if k == i:
                        result.insert(i, [h,k])
                        break
                    else:
                        if i == len(result)-1:
                            result.append([h,k])
                            break
                        else:
                            continue
        return result
        
        
            



a = Solution()
a.reconstructQueue(people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])