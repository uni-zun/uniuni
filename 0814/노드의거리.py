import sys
sys.stdin = open('input.txt','r')

from collections import deque

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

        for next in vin[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1
    return 0

for tc in range(1,T+1):
    v,e = map(int,input().split())
    vin = [[] for _ in range(v+1)]
    for i in range(e):
        start, end = map(int, input().split())
        vin[start].append(end)
        vin[end].append(start)

    s,g = map(int,input().split())
    print(f'#{tc} {bfs(v,s,g)}')

    # 다시 해야함 ㅋ
