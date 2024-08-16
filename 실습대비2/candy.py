T = int(input())

for tc in range(1,T+1):
    A, B, C = map(int, input().split())

    candy = 0
    Sehyun = True
    while Sehyun:
        if C<=B:
            B -= 1
            candy += 1
        elif B<=A:
            A -= 1
            candy += 1
        if A<B<C and A !=0:
            Sehyun = False
        elif candy >= A+B:
            candy = -1
            Sehyun = False

    print(f'#{tc} {candy}')

