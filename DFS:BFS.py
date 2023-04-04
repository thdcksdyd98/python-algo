# 대표적인 그래프 탐색 알고리즘

# 스택 자료 구조
#   -> 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조 (선입후출)
#      입구와 출구가 동일한 형태로 스택을 시각화 할 수 있다. 
# append, pop 을 사용해서 구현

# 큐 자료 구조
#   -> 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조 (선입선출)
#      입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.
# from collections import deque을 사용해서 구현 (기존 리스트로 구현이 가능하지만 비효율적)
# -> append, popleft

# DFS Depth First Search
# -> 깊이 우선 탐색. 스택 자료 구조 혹은 재귀함수를 이용하여 구현
# 동작 과정은 다음과 같음
# 1. 탐색 시작 노드를 스택에 삽입, 그리고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 '하나라도' 있다면, 그 노드를 스텍에 넣고 방문처리.
#    방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드를 꺼낸다.
# 3. 더이상 2번의 과정을 수행할 수 없을때 까지 반복. 

# [예제] 소스코드
# 각 노드가 연결된 정보를 표현 -> 대부분 그래프는 1부터 count하기 때문에 0번째 index는 empty 
graph = [
    [],         # node 0, which is not valid in this questions
    [2,3,8],    # node 1
    [1,7],      # node 2
    [1,4,5],    # node 3
    [3,5],      # node 4
    [3,4],      # node 5
    [7],        # node 6
    [2,6,8],    # node 7
    [1,7]       # node 8
]

# 각 노드가 방문된 정보를 표현
visited = [False]*9

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리-> 1 부터 시작  
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 '재귀적'으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


# BFS Breadth-First Search
# -> 너비 우선 탐색이라고 불리며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘. 큐 자료구조를 사용. 
# 동작과정은 다음과 같음
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 더 이상 2번의 과정을 수행할 수 없을 때까지 반복. 

# [예제] 소스코드 

def bfs(graph, v, visited):
    visited