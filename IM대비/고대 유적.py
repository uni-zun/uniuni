T = int(input())

# 우 하
dr = [0, 1]
dc = [1, 0]

for tc in range(1,T+1):
    N, M = map(int, input().split())
    history = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for r in range(N):
        for c in range(M):
            if history[r][c]:
                for h in range(2):
                    k = 0
                    while 0<= r+dr[h]*k < N and 0 <= c+dc[h]*k < M and history[r+dr[h]*k][c+dc[h]*k]:
                        k += 1
                    if k > max_cnt:
                        max_cnt = k

    print(f'#{tc} {max_cnt}')








