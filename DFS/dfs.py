def DFS(v):
    # print(v)
    result.append(v) #방문하는 정점번호를 리스트에 저장
    visited[v] = True #해당정점 번호가 방문한것으로 표시

    for i in range(1, 8):
        if G[v][i] and not visited[i]: #시작번호(v)에서 i번째에 값이 있고, i번호를 방문한적 없으면
            DFS(i) # i정점 방문

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
result = []
visited = [0] * 8
G = [[0]* (8) for _ in range(8)] #정점간 연결정보를 저장하는 2차원 리스트

for i in range(0, len(edges), 2): #짝수번쨰가 시작정점, 그 다음 숫자는 끝정점
    G[edges[i]][edges[i+1]] = 1 #시작정점에서 끝정점을 갈 수 있음을 표시
    G[edges[i+1]][edges[i]] = 1 #끝정점에서 시작정점으로 갈 수 있음을 표시
print(G)
DFS(1) #1번 정점부터 방문 시작
print("-".join( [str(i) for i in result]))
