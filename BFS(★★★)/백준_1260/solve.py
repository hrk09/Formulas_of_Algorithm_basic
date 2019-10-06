# 1260 bfs 문제
'''
4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4
'''

# bfs 함수 만들기
def bfs(g, start):
    q.append(start)
    while q:
        n = q.pop(0)
        if n not in visited:
            visited.append(n)
            # len(g[node])
            for i in range(1, node+1):
                if g[n][i] and i not in visited and i not in q:
                    q.append(i)
    return visited

node, edge, start = map(int, input().split())
visited = []
q = []

# edges 만들기
edges = []
for e in range(edge):
    edges.extend(map(int, input().split()))
# print(edges)

# graph 만들기(양방향)
g = [[0] * (node+1) for i in range(node+1)]
# edges의 시작점, 끝값 g에 대입하기
for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1

print(bfs(g, start))