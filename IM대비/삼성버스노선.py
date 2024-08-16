T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 노선수
    # N 개의 노선정보를 모두 읽어놓고 처리 or 읽을 때마다 처리

    counts = [0] * 5001 # 5000번 정류장까지
    for _ in range(N):
        A, B = map(int, input().split()) # Ai -> Bi 버스 노선의 시점 Ai 와 종점 Bi , Ai <= Bi
        for i in range(A, B+1): # 1 <= Ai <= Bi <= 5,000
            counts[i] += 1

    P = int(input()) # 노선수를 출력할 P 개의 버스 정류장
    # 모두 읽어놓고 처리
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end = " ")
    for j in busstop: # 노선수를 출력할 정류장 번호
        print(counts[j], end = ' ')
    print()
    '''
    1
    2
    1 3
    2 5
    5
    1
    2
    3
    4
    5
    '''