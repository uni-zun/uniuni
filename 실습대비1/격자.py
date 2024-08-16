# '#' : 검은색
# '.' : 흰색
# '?' : 둘다 가능

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = 'possible'
    for r in range(N):
        for c in range(M):
            for k in range(4):
                nr = r+dr[k]
                nc = c+dc[k]
                if 0<= nr < N and 0<= nc < M and arr[r][c] == '?':
                    if arr[nr][nc] == '#':
                        arr[r][c] = '.'
                    elif arr[nr][nc] == '.':
                        arr[r][c] = '#'
                    ??????????????????????????????????????????????



    print()
