T = int(input())

for tc in range(1, T+1):
    str = input()

    arr = []
    cnt = 0
    for i in range(len(str)):
        arr.append(str[i])
        if i-cnt>0 and arr[i-cnt] == arr[i-1-cnt]:
            arr.pop()
            arr.pop()
            cnt += 2
    print(f'#{tc} {len(arr)}')

