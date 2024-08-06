# arr1 = [0] * 3
#
# arr2 = [[0] * 3 for _ in range(2)]
# print(arr1)
# print(*arr1)
# for i in range(2):
#     print(*arr2[i])
#
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end = ' ')
#     print()

# arr = [[1,2,3], [4,5,6]]
# print(len(arr)) # 2
# print(len(arr[0])) # 3

# arr =[[0]*3]*2
# print(arr) # [[0,0,0], [0,0,0]]
# arr[0][0] = 1
# print(arr) # [[1,0,0], [1,0,0]]

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# s = 0
# for i in range(N):
#     for j in range(N):
#         s += arr[i][j]
# print(s) #48

