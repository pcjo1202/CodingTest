# DFS 알고리즘 구현 연습

# graph
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [4, 5]
]

visited = [False] * 9
# dfs - 재귀함수로 구현
# 1. 현재 노드를 방문 처리
# 2. 그래프의 현재 노드와 연결되어 있는 노드 중 우선 방문하는


def dfs(graph, v, visited):
    # 현재 노드 방문
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph[v], i, visited)


dfs(graph, 1, visited)
