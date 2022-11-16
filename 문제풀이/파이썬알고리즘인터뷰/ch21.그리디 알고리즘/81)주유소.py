# leetcode 134
'''
시간초관ㅇ린ㄷ럼일;처느라ㅓ런다;ㅣ,ㅇ라 ㅓㅗㅈ버ㅣ1 ㅃ!~!~!~~!!~!~~!~!~!~!~!~!
'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # return starting gas_station index
        start = None
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                start = i
                gas_amount = gas[i] - cost[i]
                idx = i
                flag = True
                for _ in range(len(gas)-1):
                    idx = (idx+1) % len(gas)
                    gas_amount += gas[idx] - cost[idx]
                    if gas_amount < 0:
                        flag = False
                        break
                if flag:
                    return start
        return -1

gas = [2,3,4]
cost = [3,4,3]
# cost = [3,4,5,1,2]
a = Solution()
print(a.canCompleteCircuit(gas,cost))