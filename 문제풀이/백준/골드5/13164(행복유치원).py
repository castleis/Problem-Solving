N,K = map(int,input().split())
kids = list(map(int,input().split()))
height_of_diff = []
for i in range(N-1):
    height_of_diff.append(kids[i+1] - kids[i])
# 총 K개의 조를 만들 수 있다는 뜻은, 키 차이를 K개 무시할 수 있다는 뜻
height_of_diff.sort()
print(sum(height_of_diff[:(N-K)]))