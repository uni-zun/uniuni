N = 5
arr = [55, 7, 78, 12, 42]

#각 구간의 끝 인덱스
#각 구간에서 두개씩 비교할때 왼쪽 원소의 인덱스l
#왼쪽원소가 더 크면 교환
for i in range(N-1, 0, -1): # 각 구간의 끝 인덱스 i
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)