import sys
sys.stdin = open("input.txt", "r")

di = [-1, 0, 0]
dj = [0, 1, -1]

for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #ladder[99].index(2)
    d=0

    i,j = 99,ladder[99].index(2)

    while i != 0:
        if 0 <= i < 100 and 0 < j < 99 and ladder[i+di[d]][j+dj[d]] != 0:
            i += di[d]
            j += dj[d]
        elif j == 0 and ladder[i+di[d]][j+dj[d]] == 0:
            d
        else:
            d += 1
            if d > 2:
                d = 0


