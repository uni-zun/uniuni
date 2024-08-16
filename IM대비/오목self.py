# 우, 우하, 하 , 좌하
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

T = int(input())


for tc in range(1,T+1):
    N = int(input())
    ans = 'NO'

    board = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for d in range(4):
                cnt = 0
                for k in range(5):
                    nr = r + dr[d]*k
                    nc = c + dc[d]*k
                    if 0<= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                        cnt += 1
                        if cnt == 5:
                            ans = 'YES'

    print(f'#{tc} {ans}')







