def bfs(v):
    q.append(v)
    while q:
        node = q.pop(0)
        if node not in visited:
            visited.append(node)
            for i in range(8):
                if g[node][i] and i not in visited and i not in q:
                    q.append(i)
    return visited

# edge 받고, 양방향 그래프(g) 만들기
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

g = [[0]*8 for i in range(8)]
visited = []
q = []
for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1

print(bfs(1))