'''
1부터 10까지 출력해보기
반복문 -> 재귀호출
'''

# n = 10
#
# # 시작 : 1
# # 종료 : 10
# # 값의 변화량 +1
# # 값을 나타내기 위해 사용하는 변수 : i
# for i in range(1,n+1):
#     print(i, end=" ")
# print()
#
# # 시작 : 1
# # 종료 : 10
# # 값의 변화량 : +1
# # 값을 나타내기 위해 사용하는 변수 : j
# def myprint(j, n):
#     if j > n:
#         return
#     # 1. 종료 조건
#
#     # 2. 재귀 호출(자기 자신함수, 여기서는 myprint)
#     # 필요한 작업을 수행한 후에
#     print(j, end=' ')
#     myprint(j+1,n)
#     return
    # 종료 조건에 점점 가까워 지도록 재귀 호출을 해줘야한다.
    # 인자를 통해서 가까워 질수 있도록 한다.

# 재귀호출 시작
# myprint(1, n)

'''
재귀함수를 통해 2차원 배열 행 우선 순회해보기
'''
n = 4
N = 5
arr = [[N*j+i for i in range(1,N+1)] for j in range(N)] # 1~25
# 1 2 3 4 5
# 6 7 8 9 10
# ...
# 21 22 23 24 25
def recul(i, j, N):
    if i > N-1:
        return
    elif j > N-1:
        print()
        return recul(i+1, 0, N)
    else:
        print(arr[i][j], end=" ")

    recul(i, j+1, N)
recul(0, 0, N)