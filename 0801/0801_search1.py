import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input()) # 달팽이 크기

    snail = [[0] * N for _ in range(N)]

    #방향
    d = 0

    r, c = 0, 0 # 현재 위치 (0,0)에서 시작
    for i in range(1, N**2+1):
        snail[r][c] = i

        if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and snail[r+dr[d]][c+dc[d]] == 0:
            r += dr[d]
            c += dc[d]
        else:
            d += 1
            if d > 3:
                d = 0
            # d = (d+1)%4

            r += dr[d]
            c += dc[d]

    print(f'#{tc}')

    for r in range(N):
        print(*snail[r])


        # 방향을 언제 바꿔야할까?
        # 배열의 범위를 벗어났을때
        # 내가 이전에 놓은 숫자를 만났을때