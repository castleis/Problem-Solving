# BFS
'''
BFS란! -> 현재 노드에서 방문하지 않은 모든 인접노드를 스택에 넣고, 차례대로 계속 방문하는거잖여
탐색의 시작점 -> 1부터 가야하지 않을까? 1은 어떻게 찾을까
그래프 간선들은 어떻게? -> visited = [0]*6
!!!!! 아마도 내가 구해야되는건 그래프의 level인 것 같은디!! (https://hanyeop.tistory.com/113) : BFS로 그래프의 level 구하기
익을 수 없는 토마토를 어떻게 잘 찾을 수 있을까!! 3중 for문은 너무 오래걸리는 것 같다 (시간초과) 시간을 어떻게 줄일 수 있을까아아ㅏ아아

숫자를 입력받을 때 너무 많다면 int로 바꾸지 말고 그냥 str로 받아서 문자로 활용하는건 어떨까? 1등코드 보니까 map(int()) 안해주고 그냥 받아서 문자열로 쓰네유
'''
import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())
box,cantRipe = [],[]
isRipe = deque([])
for z in range(H):
	layer = []
	for y in range(N):
		layer.append(list(map(int,input().split())))
		for x in range(M):
			if layer[y][x] == 1 :
					isRipe.append([z,y,x])
			elif layer[y][x] == -1:
				cantRipe.append([z,y,x])
	box.append(layer)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def cant(cantRipe):
	while cantRipe:
		unriped = cantRipe.pop()
		z,y,x = unriped[0], unriped[1], unriped[2]
		for i in range(6):
			if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N and 0 <= z+dz[i] < H:
				if box[z+dz[i]][y+dy[i]][x+dx[i]] == 0:
					return 0
	else:
		return 1

def is_Ripe(box,isRipe,day = 0):
	while isRipe:
		# print(f'{day}일째 : {isRipe}')
		for _ in range(len(isRipe)):
			here = isRipe.popleft()
			z, y, x = here[0], here[1], here[2]
			# print(f'현재위치 : {here},{queue}')
			for i in range(6):
				if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N and 0 <= z+dz[i] < H:
					if box[z+dz[i]][y+dy[i]][x+dx[i]] == 0:
						box[z+dz[i]][y+dy[i]][x+dx[i]] = 1
						isRipe.append([z+dz[i],y+dy[i],x+dx[i]])		
		day += 1
	if not cant(cantRipe):
		return -1
	return day-1
print(is_Ripe(box,isRipe))
