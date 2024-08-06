# for i in range(1, 11):
#     n = int(input())
#     bds = list(map(int, input().split()))
#     result = 0
#
#     for idx in range(2, n - 2):
#         height = 0
#         for near in range(5):
#             if near != 2:
#                 if bds[idx - 2 + near] > height:
#                     height = bds[idx - 2 + near]
#         if bds[idx] - height > 0:
#             result += bds[idx] - height
#
#     print(f'#{i} {result}')

T = 10
for tc in range(1, T+1):
    n = int(input())

    buildings = list(map(int,input().split()))

    count = 0 # 조망권 개수

    for i in range(2, n-2):
        height = buildings[i] # i 위치에 있는 건물의 높이
        for j in range(height, -1, -1): #위층 부터 검사(조망권 없는 위치 나오면 그 밑은 볼 필요 없기 때문에)
            # j => 층의 높이
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]:
                count += 1
            else:
                # 만약 건물 하나라도 지금 층 보다 높으면 검사 할 필요 x
                break


