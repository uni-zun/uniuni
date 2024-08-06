T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_num = arr[0]
    for i in range(N):
        if max_num < arr[i]:
            max_num = arr[i]

    min_num = arr[0]
    for j in range(N):
        if min_num > arr[j]:
            min_num = arr[j]
    print(f'#{tc} {max_num - min_num}')
