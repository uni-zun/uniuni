import sys
sys.stdin = open("input.txt", "r", encoding="utf-8")

T= 10

for tc in range(1,T+1):
    input()

    P = input() #우리가 찾는 문자열 패턴
    T = input() #전체 텍스트

    count = 0 # 전체 텍스트(T) 안에 우리가 찾는 문자열 패턴 (P)가 몇개?

    pl = len(P) # 패턴의 길이
    tl = len(T) # 텍스트의 길이

    pi = 0 # 패턴 순회 전용 인덱스
    ti = 0 # 텍스트 순회 전용 인덱스

    while pi < pl and ti < tl:
        # P[pi] 와 T[ti] 를 비교해서
        # 같다? pi, ti 둘다 1씩 증가
        # 다르다? 앞으로 돌아가서 다시 비교

        if T[ti] != P[pi]:
            # 다음 비교 시작 위치 = 현재 비교 위치 - 내가 비교한 횟수(pi)
            # 텍스트 비교 시작 위치 = ti - pi
            ti = ti - pi
            pi = -1

        ti += 1
        pi += 1

        #pi 가 패턴의 길이만큼 되어버렸다면??
        # => 중간에 달랐던적이 없었다. => 패턴을 발견했다 !
        if pi == pl :
            count += 1

            # 다음 비교를 위해서 다음 비교 시작 위치로 이동
            ti = ti - pi + 1
            pi = -1 +1

    print(f'#{tc} {count}')