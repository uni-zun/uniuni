import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# arr = [[0]*10 for _ in range(10)]

for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for k in range(N):
        color_list = list(map(int, input().split()))
        for i in range(color_list[0], color_list[2]+1):
            for j in range(color_list[1], color_list[3]+1):
                arr[i][j] += 1

