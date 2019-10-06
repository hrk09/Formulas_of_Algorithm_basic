# 값 받기
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# dfs 함수 만들기
def dfs(v):
    # 스택에 시작값 넣기
    stack.append(v)
    # v 방문처리
    visited[v] = 1
    # 1번부터 7까지 돌면서
    for i in range(1, 8):
        # 시작번호 v 에서 i 번째에 값이 있고, i 방문한 적이 없으면,
        if g[v][i] and not visited[i]:
            # i 방문한다(i부터 다시 dfs 돌린다)
            dfs(i)
    return stack

stack = []
visited = [0] * 8
# base graph 만들기
g = [[0] * 8 for i in range(8)]
# 양방향 그래프 만들기
for i in range(0, len(edges), 2):
    # 정방향
    g[edges[i]][edges[i+1]] = 1
    # 역방향
    g[edges[i+1]][edges[i]] = 1
print(g)
print(dfs(1))
res = dfs(1)
print(' '.join([str(i) for i in stack]))