T = 10

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    front = 0
    while numbers[front]:
        for i in range(1,6):
            numbers[front] -= i
            if numbers[front] <= 0:
                numbers[front] = 0
                break
            front = (front + 1) % 8
    result = []
    for j in range(1,9):
        result.append(numbers[(front + j) % 8])
    print(f'#{tc}', *result)

