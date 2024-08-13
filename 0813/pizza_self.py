T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    qsize = N + 1
    oven = [0]*qsize
    front = rear = 0

    for i in range(N):
        rear = (rear + 1)% qsize
        oven[rear] = i

    next_pizza = N
    pizza_num = 0

    while front != rear:
        front = (front+1) % qsize
        pizza_num = oven[front]

        pizza[pizza_num] //= 2

        if pizza[pizza_num] > 0:
            rear = (rear+1) % qsize
            oven[rear] = pizza_num

        else:
            if next_pizza < M:
                rear = (rear + 1)% qsize
                oven[rear] = next_pizza
                next_pizza += 1

    print(f'#{tc} {pizza_num+1}')