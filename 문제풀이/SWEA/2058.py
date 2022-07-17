str_list = list(map(str, input()))
int_list = list(map(int, str_list))
answer = 0
for i in int_list:
    answer += i
print(answer)