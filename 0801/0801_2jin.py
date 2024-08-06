import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    P, A, B = map(int, input().split())
    # P : 전체 쪽수 , A , B : 찾아야 하는 쪽수
    A_count = 0
    B_count = 0

    A_start = 1
    A_end = P
    A_mid = (A_start + A_end)//2

    B_start = 1
    B_end = P
    B_mid = (B_start + B_end)//2

    while A != A_mid:
        if A_mid < A:
            A_start = A_mid
            A_mid = (A_start + A_end)//2
        elif A_mid > A:
            A_end = A_mid
            A_mid = (A_start + A_end)//2
        A_count += 1
    while B != B_mid:
        if B_mid < B:
            B_start = B_mid
            B_mid = (B_start + B_end)//2
        elif B_mid > B:
            B_end = B_mid
            B_mid = (B_start + B_end)//2
        B_count += 1
    if A_count > B_count:
        print(f'#{tc} B')
    elif A_count < B_count:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

