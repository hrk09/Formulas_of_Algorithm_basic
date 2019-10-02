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
# dfs 함수
def dfs(start):
    stack.append(start)
    visit[start] = 1
    for i in range(1, node+1):
        if g[start][i] and not visit[i]:
            dfs(i)
    return stack

# bfs 함수
def bfs(g, start):
    visited = []
    q = []
    q.append(start)
    while q:
        n = q.pop(0)
        if n not in visited:
            visited.append(n)
            for i in range(node+1):
                if g[n][i] and i not in visited and i not in q:
                    q.append(i)
    return visited

node, edge, start = map(int, input().split())

# edges 받기
edges = []
for e in range(edge):
    edges.extend(map(int, input().split()))
# print(edges)

visit = [0]*(node+1)
stack = []

# 양방향 그래프 만들기/ 대입
g = [[0] * (node+1) for i in range(node+1)]
for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1

res1 = dfs(start)
res2 = bfs(g, start)
print(' '.join([str(i) for i in res1]))
print(' '.join([str(i) for i in res2]))