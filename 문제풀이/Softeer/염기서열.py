N,M = map(int, input().split())
DNAs = [list(input()) for _ in range(N)]
rep = [i for i in range(N)]

for i in range(N-1):
    print(f'=========================== {i} ======================')
    if rep[i] != i:
        continue
    same_dna = [False]*(i) + [True]*(N-i)
    for m in range(M):
        print(f'===== {m} --- {DNAs[i][m]}')
        if DNAs[i][m] == '.':
            continue
        for j in range(i+1, N):
            print(f'={j}')
            if same_dna[j] == False or rep[j] != j:
                same_dna[j] = False
                print(f'다른 초염기서열 혹은 이미 속한 염기서열')
                continue
            if DNAs[j][m] == DNAs[i][m] or DNAs[j][m] == '.':
                pass
            else:
                print(f'DNAs[{j}][{m}] = {DNAs[j][m]} : 다른 초염기서열')
                same_dna[j] = False
    print(rep)
    for n in range(N):
        if same_dna[n]:
            rep[n] = i
    print('same_dna : ', same_dna)
    print('rep : ', rep)

def find(x):
    if x == rep[x]: 
        return x
    else:
        x = rep[x]
        find(x)

print(rep)
for i in range(N):
    rep[i] = find(i)

print(rep)
# print(len(list(set(rep))))