import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    min_arr = []
    max_arr = []
    result = []
    if N%2 == 0:
        for min_num in range(N//2):
            min_arr.append(arr[min_num])
        for max_num in range(N-1, N//2-1,-1):
            max_arr.append(arr[max_num])
        for k in range(N//2):
            result.append(max_arr[k])
            result.append(min_arr[k])
    else:
        for min_num in range(N//2):
            min_arr.append(arr[min_num])
        for max_num in range(N-1, N//2,-1):
            max_arr.append(arr[max_num])
        for k in range(N//2):
            result.append(max_arr[k])
            result.append(min_arr[k])
        result.append(arr[N//2])
    print(f'#{tc} ', end="")
    for r in range(10):
        print(result[r], end=" ")
    print()