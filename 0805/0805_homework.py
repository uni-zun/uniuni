import sys
sys.stdin = open("input.txt", "r")

T = 10

for tc in (1,T+1):
    N = int(input())

    arr =[list(input()) for _ in range(8)]

    count = 0

    for i in range(8-N+1):
        for j in range(8-N+1):
            cnt = 0
            for k in range(N//2):
                if arr[i][j+k] == arr[i][j+N-1-k]:
                    cnt += 1
                    if cnt == N//2:
                        count += 1

    print(count)