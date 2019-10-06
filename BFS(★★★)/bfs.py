# bfs 구현시 유의사항
# dfs와 다르게 재귀호출을 사용하지 않는다는 것 큐를 이용해 iteractive하게 구현함

def BFS(graph, v):# 그래프 G, 탐색 시작점 v
    q = []
    q.append(v)
    while q: # 큐에 값이 있으면 실행
        node = q.pop(0)# 큐의 첫번째 원소 반환
        if node not in visited:# 방문되지 않은 곳이라면
            visited.append(node)# visit에 node 추가
            for i in range(1, len(G[node])):
                # 해당 노드의 i 번째 값이 있고, i 가 방문한 적이 없고, q에도 없으면, q에 하나 더함
                if G[node][i] and i not in visited and i not in q:
                    q.append(i)
    return visited


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
result = []
visited = []
G = [[0]* (8) for _ in range(8)] #정점간 연결정보를 저장하는 2차원 리스트

for i in range(0, len(edges), 2): #짝수번쨰가 시작정점, 그 다음 숫자는 끝정점
    G[edges[i]][edges[i+1]] = 1 #시작정점에서 끝정점을 갈 수 있음을 표시
    G[edges[i+1]][edges[i]] = 1 #끝정점에서 시작정점으로 갈 수 있음을 표시
result = BFS(G,1) #1번 정점부터 방문 시작
print(result)
# print("-".join( [str(i) for i in result]))