
T = 10


def get_result(numbers):
    stack = []

    for token in numbers:
        if token not in "+":
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            result = 0
            if token == '+':
                result = left + right
            stack.append(result)

    return stack.pop()

for tc in range(1,T+1):
    N = int(input())

    str = input()
    plus = []
    numbers = []
    for i in range(N):
        if i%2:
            plus.append(str[i])
        else:
            numbers.append(str[i])
    numbers.extend(plus)



    result = get_result(numbers)

    print(f'#{tc} {result}')