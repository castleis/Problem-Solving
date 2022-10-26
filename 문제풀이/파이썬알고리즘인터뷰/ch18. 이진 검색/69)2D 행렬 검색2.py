class Solution:
    def searchMatrix(self, matrix, target):
        arr = []
        for lst in matrix:
            arr += lst
        arr.sort()
        S,L = 0, len(arr)-1
        while S <= L:
            idx = (S+L) // 2
            if arr[idx] == target:
                return True
            elif arr[idx] > target:
                L -= 1
            else:
                S += 1
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20