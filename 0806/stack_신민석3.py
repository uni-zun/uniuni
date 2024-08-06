T = int(input())

for tc in range(1,T+1):
    check = input()

    stack = []

    # 괄호 검사 결과 : 1이면 ok, 0이면 err
    answer = 1

    # 괄호 검사
    # check 에서 한글자씩 떼어와서 검사
    for c in check:
        # 1. c가 여는 괄호인가??(왼쪽) => 스택에 push
        if c == '(':
            stack.append(c)
        # 2. c가 닫는 괄호인가??(오른쪽)
        elif c ==')' and stack:
            stack.pop()
        elif c ==')' and not stack:
            answer = 0
    if stack:
        answer = 0
        # 스택에서 꺼내기전에 스택이 비어있나 확인 => 스택이 비어있으면 err

    print(f'#{tc} {answer}')

'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
'''