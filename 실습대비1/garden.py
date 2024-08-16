T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())
    water = [0]*N
    W = 2*D+1
    cnt = 0
    for i in range(D,N,W):
        water[i] = 1
        cnt += 1
    if cnt * W < N:
        cnt += 1

    print(f'#{tc} {cnt}')