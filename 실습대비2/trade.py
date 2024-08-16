T = int(input())

for tc in range(1,T+1):
    n = int(input())
    day = list(map(int, input().split()))

    study = 0
    week = 0
    while n != study:
            for i in range(7):
                if day[i]:
                    study += 1
                    if n == study:
                        week = week*7+(i+1)
                        break
            if n != study:
                week += 1
    if not day[0]:
        week -= day.index(1)
    print(f'#{tc} {week}')
