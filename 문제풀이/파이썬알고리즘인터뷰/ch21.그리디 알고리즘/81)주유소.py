# leetcode 134
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # return starting gas_station index
        if sum(gas) < sum(cost):
            return -1
        start, gas_amount = 0,0
        for i in range(len(gas)):
            if gas[i] + gas_amount < cost[i]:
                start = i + 1
                gas_amount = 0
            else:
                gas_amount += gas[i] - cost[i]
        return start

gas = [2,3,4]
cost = [3,4,3]
# cost = [3,4,5,1,2]
a = Solution()
print(a.canCompleteCircuit(gas,cost))