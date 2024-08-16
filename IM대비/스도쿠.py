T = int(input())

di = [0, 0, 1, 1, 0, 0, -1, 0,-1]
dj = [1, 1, 0, 0, -1, -1, 0, 1,-1]

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    num = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        hang = []
        yeol = []
        for j in range(9):
            hang.append(sudoku[i][j])
            yeol.append(sudoku[j][i])
        if sorted(hang) == num and sorted(yeol) == num:
            cnt += 2
    for a in range(0,9,3):
        for b in range(0,9,3):
            square = [sudoku[a][b]]
            for k in range(9):
                a += di[k]
                b += dj[k]
                if k<8:
                    square.append(sudoku[a][b])
                    if sorted(square) == num:
                        cnt += 1
    if cnt == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')