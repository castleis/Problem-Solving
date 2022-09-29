# leetcode 310
'''
핵심 아이디어 -> 단계별로 리프 노드를 제거
제일 끝에 있는 리프노드들을 단계별로 제거하다보면 마지막에 남는 노드가 루트노드가 되었을 때 최소 높이가 됨을 알 수 있음
'''
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # n이 1 이하이면 바로 0 리턴
        if n <= 1:
            return [0]

        # 무방향 그래프 만들기
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # 리프 노드들을 찾아 저장, graph[i]에 하나만 들어있다면 리프노드라는 의미
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        # 마지막으로 2개가 남는다면 모두 루트 노드가 될 수 있으므로 n이 2 이상일 때까지
        while n > 2:
            # 현재 리프노드들을 제거하고 새로운 리프노드가 될 노드들을 담아줄 리스트
            new = []
            for leaf in leaves:
                # 무방향 그래프이므로 양쪽 방향에서 모두 삭제
                nextt = graph[leaf].pop()
                graph[nextt].remove(leaf)
                
                # 리프노드를 삭제한 곳이 새로운 리프노드인지 확인
                if len(graph[nextt]) == 1:
                    new.append(nextt)
            # 삭제한 리프노드만큼 n에서 빼줌
            n -= len(leaves)
            # 새로운 노드들을 leaves에 할당하고 다시 반복
            leaves = new
        # 마지막으로 leaves에 남은 노드들을 출력 -> 루트 노드 후보
        return leaves