def make_subset(c, selected, result, n):
    global min_sum
    s =0
    for num in result:
        s += num
    if c == n:
        if s < min_sum:
            min_sum = s
        return
    if s >= min_sum:
        return
    for r in range(N):
        if not selected[r]:
            selected[r] = 1
            result.append(arr[r][c])
            make_subset(c+1, selected, result, n)
            selected[r] = 0
            result.pop()


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9223372036854775807
    make_subset(0,[0]*N ,[], N)
    print(f'#{tc} {min_sum}')
