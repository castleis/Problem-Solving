
num_of_house = int(input())
firewalls_radius = list(map(int,input().split()))
firewalls_radius.sort()
cnt_house = 1

for radius in range(2, firewalls_radius[-1] + 1):
    cnt = 0
    for j in range(num_of_house):
        if firewalls_radius[j] >= radius and firewalls_radius[j] % radius == 0:
            cnt += 1
    if cnt > cnt_house:
        cnt_house = cnt

print(cnt_house)
