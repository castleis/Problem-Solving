def ducks(start):
    global cnt
    quack = 'quack'
    j = 0
    check = False
    for i in range(start,length):
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = 1
            if duck[i] == 'k':
                if not check:
                    cnt += 1
                    check = True
                j = 0
                continue
            j += 1
    return

duck = input().strip()
length = len(duck)
visited = [0]*length
cnt = 0
if length % 5 != 0 or duck[0] != 'q':
    print(-1)
    quit()
for i in range(length):
    if duck[i] == 'q' and not visited[i]:
        ducks(i)
        # print(visited)
if not cnt or not all(visited):
    print(-1)
else:
    print(cnt)