import sys
sys.stdin = open("input.txt", "r")

# 버스를 운행하는 함수
def drive(K, N):
    # return 0 : 충전소가 제대로 배치되지 않아서 운행 불가능
    # return > 0 : 충전소가 제대로 배치되어서 충전한 횟수를 리턴

    last = 0 # 마지막으로 충전한 위치 (운행 불가능한 상황 판별)
    now = K # 현재 버스 위치(정류장 번호), 처음에 충전된 상태로 간다고 했으니까 K만큼 미리 이동
    count = 0 # 충전 횟수

    # 버스 운행 하기
    # 1. 일단 최대로 간다(K만큼)
    # 2-1. 충전기가 있으면 1로가서 반복
    # 2-2. 충전기가 없으면 앞으로 한칸 들어오기
    # 2-2-1. 충전기가 있으면 1로가서 반복
    # 2-2-2. 충전기가 없으면 앞으로 한칸 돌아오기
    # ...
    # 원래 위치로 돌아와 버리면 운행 불가능
    # 현재 위치가 마지막 정류장위치 이상 이면 운행 가능

    while now < N:

        # 현재 위치에 충전기가 있나 없나 검사
        # 만약 없으면 충전기가 있는 곳까지 한칸씩 이동
        while stop[now] == 0:
            now -= 1
            # 뒤로가다가 마지막 충전 위치로 와버리면 운행 불가
            if now == last:
                # 운행 불가, 이 이상 진행 할 필요 없으니 함수 종료
                return 0
        # 여기 코드가 실행되면 중간에 충전기를 만났다는 것이다.
        # 마지막 충전 위치 갱신
        last = now
        # 다음 위치로 이동(최대한 이동 해야 하니까 K만큼)
        now += K
        # 충전 횟수 증가
        count += 1

    # 여기 코드가 실행되면 반복문이 잘 종료가 되었다(중단없이)
    # now >= N 이라는것 -> 제대로 도착 했다는것
    return count

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    # K : 충전한번당 이동 할수있는 정류장 최대 수 , N : 정류장 개수, M : 설치된 충전소 개수

    # 충전기의 위치 모음(리스트)
    charge_list = list(map(int, input().split()))

    # 정류장에 충전소가 있나 없나 여부를 나타내는 리스트
    stop = [0] * N
    # stop[i] => i 번째 정류장에 충전기가 있나 없나 를 나타낸다.
    # stop[i] == 1 : i번 정류장에는 충전기가 있다.
    # stop[i] == 0 : i번 정류장에는 충전기가 없다.

    for x in charge_list:
        stop[x] = 1 # x번 정류장에는 충전소가 있다.

    answer = drive(K,N)
    print(f'#{tc} {answer}')





