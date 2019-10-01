import sys
sys.stdin = open('input.txt', 'r')

# dfs 함수
def dfs(v):
    stack.append(v)
    visited[v] = 1
    for i in range(1, node+1):
        if g[v][i] and not visited[i]:
            dfs(i)
    return stack

# 값 받기
node, edge, start = map(int, input().split())
edges = []
for n in range(edge):
    edges.extend(map(int, input().split()))
# print(edges)

# stack, visited 기본작업
stack = []
visited = [0]*(node+1)

# 양방향 그래프 만들기
g = [[0] * (node+1) for i in range(node+1)]
# print(g)

for i in range(0, len(edges), 2):
    # 정방향
    g[edges[i]][edges[i+1]] = 1
    # 역방향
    g[edges[i+1]][edges[i]] = 1
# print(g)
dfs(start)
print(' '.join([str(i) for i in stack]))