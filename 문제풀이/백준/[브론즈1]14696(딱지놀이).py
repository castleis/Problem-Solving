n = int(input())

for _ in range(n):
    arr_a = sorted(input().split()[1:], reverse = True)
    arr_b = sorted(input().split()[1:], reverse = True)
    print(arr_a)
    print(arr_b)
    if arr_a > arr_b :
        print('A')
    elif arr_b > arr_a:
        print('B')
    else :
        print('D')
    

# def count(arr):
#     dict = {1:0,2:0,3:0,4:0}
#     for i in range(1,5):
#         for j in range(len(arr[1:])):
#             if arr[1:][j] == i :
#                 dict[i] += 1
#     return dict

# def winner(dict1,dict2):
#     for i in range(4,0,-1):
#         a = dict1[i]
#         b = dict2[i]
#         # print(i,a,b)
#         if a > b :
#             return 'A'
#         elif a == b:
#             continue
#         else :
#             return 'B'
#     return 'D'

    

# for i in range(n):
#     a_dict = count(arr_a[i])
#     b_dict = count(arr_b[i])
#     print(winner(a_dict,b_dict))

