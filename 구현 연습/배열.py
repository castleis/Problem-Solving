# N = 3
# M = 4
# # N개의 원소를 갖는 0으로 초기화된 1차원 배열
# arr1 = [0] * N
# print(arr1)
# # 크기가 NxM이고 0으로 초기화 된 2차원 배열
# arr2 = [[0] * M for _ in range(N)]
# print(arr2)

'''
arr3 = [[0]*M]*N
print(arr3)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr3[1][1] = 1
print(arr3)  # [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
-> 얕은복사이기 때문에 모든 행의 [1]번째가 1로 바뀐다.
'''
arr1 = []
arr1.extend(list(map(int,input().split())) for _ in range(5))

arr = [[0]*5 for _ in range(5)]
i = 25
di = [0,1,0,-1]
dj = [-1,0,1,0]
arr[2][2] == i
a,b,k = 2,2,0
while i > 0:
    for j in range(4):
        k += 1
        for _ in range(k):
            i -= 1
            a += di[j]
            b += dj[j]
            print(f'a,b,j,i : {a},{b},{j},{i}')
            arr[a][b] = i
            print(arr)

print(arr)


