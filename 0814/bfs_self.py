from collections import deque

'''
정점의 개수 : V , 간선의 개수 : E
V = 7, E = 8
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

T = int(input())

def bfs(G, V, N):
    visited = [0] * (N+1)
    q = deque()
    q.append(V)
    visited[V] = 1

    while q:
        now = q.popleft()
        if now == N:
            return visited[now] - 1

        for next in G[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1
    return 0

for tc in range(1,T+1):
    v,e = map(int,input().split())
    G = [[] for _ in range(v+1)]
    for i in range(e):
        start, end = map(int, input().split())
        G[start].append(end)
        G[end].append(start)
    s,g = map(int,input().split())
    print(f'#{tc} {bfs(v,s,g)}')