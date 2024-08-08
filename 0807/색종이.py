def paper(N):

    if N <= 0:
        return 0

    if N == 10:
        return 1
    elif N == 20:
        return 3


    if N > 20:
        if N % 20 == 0:
            return paper(N - 20) * 4 + 1
        elif N % 20 == 10:
            return paper(N - 20) * 4 + 1

    return 0



T = int(input())

for tc in range(1,T +1):
    N = int(input())
    print(f'#{tc} {paper(N)}')

