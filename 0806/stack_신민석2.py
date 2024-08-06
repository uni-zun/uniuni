# top 과 크기가 고정된 자료구조인 배열을 활용해서 스택 만들기

# 스택 초기화
# top : 스택에 마지막으로 삽입된 원소의 위치(인덱스) 를 나타낸다.
top = -1
# 스택의 크기
N = 10
# 스택 만들기
s = [0]*N

# 스택에 원소 삽입하기
for i in range(1,N+1):
    top += 1 # 삽입 전에 마지막 위치 +1
    s[top] = i # top 위치에 원소를 삽입

print(s)
# 원소를 삽입하기 전에 스택이 다 찼나 확인
if top < N-1:
    top += 1
    s[top] = 11
else:
    print("overflow")

print(top, s)

# 스택에서 원소 삭제
for i in range(10):
    print(s[top], end=' ')
    top -= 1
print()

# 크기가 고정된 배열과 top 을 통해서 스택을 구현한 경우
# 배열안의 원소가 "진짜" 삭제 되지 않는다.

# top 을 보고 스택이 비었는지 여부를 판단!
# [1,2,3,4,5] 이렇게 되어 있어도 top = -1 이면 비어있다고 판단해야 한다.

print(top, s)
