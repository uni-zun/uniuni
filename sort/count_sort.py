DATA = [0, 4, 1, 3, 1, 2, 4, 1]

counts = [0]*5 # DATA 가 0~4까지의 정수

N = len(DATA) # DATA 의 크기
TEMP = [0] * N # 정렬된 결과 저장

# 1단계 : DATA 원소 별 개수 세기
for x in DATA: # DATA 의 원소 x 를 가져와서 counts[x]에 개수 기록
    counts[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5): # count[0]~count[4] 까지 누적개수
    counts[i] = counts[i-1] + counts[i]

# 3단계 : DATA 의 맨 뒤부터 TEMP 에 자리 잡기
for i in range(N-1, -1, -1):
    counts[DATA[i]] -= 1  # 누적개수 1개 감소
    TEMP[counts[DATA[i]]] = DATA[i]
print(TEMP)

# def counting_sort (DATA, TEMP, K):
#     # DATA : 정렬 대상(배열)
#     # TEMP : 정렬 결과(배열)
#     # K : 정렬 대상 중 최댓값 = 카운트 배열의 크기
#     COUNT = [0] * (K+1)
#     # COUNT : 카운트 배열(등장하는 원소의 개수를 세기 위해)
#     # C[X] = X의 등장 횟수
#     # C[1] => DATA 안에 1이 몇개 있는가를 말해준다.

#     # 1. 각 원소의 등장 횟수를 카운트
#     for num in DATA:
#         # DATA 배열 안에서 꺼내온 숫자 num 의 등장 횟수 +1
#         COUNT[num] += 1

#     # 2. 각 원소의 등장횟수를 계산해서 각 원소가 들어갈 자리 위치를 계산
#     # 내 앞자리 + 현재 나의 등장 횟수 ... 누적적
#     for i in range(1, len(COUNT)):
#         COUNT[i] = COUNT[i] + COUNT[i-1]

#     # 3. 뒤에서부터 DATA 를 확인하면서 COUNT 를 보고 자리를 확인
#     # COUNT 의 숫자 -1 하고 그 위치에 넣는다.

#     for i in range(len(DATA) -1, -1, -1):
#         # 자리에 놓기 전에 -1(자리 겹치는거 방지)
#         # DATA[i] 번째 친구의 자리 번호
#         COUNT[DATA[i]] -= 1

#         # COUNT[DATA[i]] => DATA[i] 원소가 들어갈 자리번호(인덱스)
#         TEMP[COUNT[DATA[i]]] = DATA[i]

# nums = [0, 4, 1, 3, 1, 2, 4, 1]
# result = [0]*8 #정렬 결과

# counting_sort(nums, result, max(nums))
# print(result)