import sys
sys.stdin = open("input.txt", "r")

T =int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    answer = ''
    for i in range(N):
        same_count1 = 0
        same_count2 = 0
        same_count3 = 0
        same_count4 = 0

        result = []
        for k in range(N - M + 1):
            if N == M:
                for j in range(M//2):
                    if arr[i][j] == arr[i][M-1-j]: # 가로
                        same_count1 += 1
                        if same_count1 == M//2:
                            result = arr[i]
                    elif arr[j][i] == arr[M-1-j][i]: # 세로
                        same_count2 += 1
                        if same_count2 == M//2:
                            for a in range(M):
                                result.append(arr[a][i])

            if N != M:
                for j in range(M//2):
                    if arr[i][j+k] == arr[i][M-1-j+k]:
                        same_count3 += 1
                        if same_count3 == M//2:
                            for num in range(M):
                                result.append(arr[i][k+num])


                    elif arr[j+k][i] == arr[M-1-j+k][i]:
                         same_count4 += 1
                         if same_count4 == M//2:
                             for b in range(M):
                                result.append(arr[k+b][i])


        if result:
            answer = ''.join(result)

    print(f'#{tc} {answer}')
