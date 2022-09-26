w,h = map(int,input().split())
N = int(input())
cut_w, cut_h = [0],[0]
for _ in range(N):
    cut = list(map(int,input().split()))
    if cut[0] == 0:
        cut_w.append(cut[1])
    else :
        cut_h.append(cut[1])
cut_w.sort()
cut_w.append(h)
cut_h.sort()
cut_h.append(w)

max_w, max_h = 0,0
for i in range(len(cut_w)-1):
    a = cut_w[i+1] - cut_w[i]
    if max_w < a:
        max_w = a

for j in range(len(cut_h)-1):
    b = cut_h[j+1] - cut_h[j]
    if max_h < b:
        max_h = b

print(max_w * max_h)
