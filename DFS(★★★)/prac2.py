# bfs
def bfs(s):
    q.append(s)
    while q:
        n = q.pop(0)
        # 원소 맨앞 꺼 뽑은 것이 방문한 기록이 없고
        if n not in visit:
            visit.append(n)
            # n과 연결된 것들 중
            for i in range(8):
                if g[n][i] and i not in visit and i not in q:
                    q.append(i)
    return visit


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
n = 7
g = [[0]*(n+1) for i in range(n+1)]
# print(g)
q =[]
visit = []

for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1

print(bfs(1))