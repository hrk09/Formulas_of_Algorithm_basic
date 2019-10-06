# 1260 dfs 문제
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

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        vertex = stack.pop()
        v = vertex
        if v not in visited:
            visited.append(v)
            if v in graph:
                tmp = list(set(graph[v]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    return ' '.join(str(i) for i in visited)

# graph 딕셔너리 만들기(양방향)
graph = {}
node, edge, start = map(int, input().split())

for i in range(edge):
    n1, n2 = map(int, input().split())
    # graph 에 n1이 없으면, n1: n2 넣기
    if n1 not in graph:
        graph[n1] = [n2]
    # 중복 없이 넣는 것, 이미 그 값이 있으면 안넣어도 됨
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    # 양방향 넣기
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(dfs(graph, start))