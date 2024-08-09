icp = {"+":1, "-":1, "*":2, "/":2, "(":3 }
isp = {"+":1, "-":1, "*":2, "/":2, "(":0 }

def get_postfix(infix, n):
    postfix = ""
    stack = []
    for i in range(n):
        if infix[i] not in "(+-*/)":
            postfix += infix[i]
        else:
            if infix[i] == ")":
                while stack:
                    op = stack.pop()
                    if op == "(":
                        break

                    postfix += op
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []
    for token in postfix:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            result = 0
            if token == '+':
                result = left + right
            if token == '-':
                result = left - right
            if token == '*':
                result = left * right
            if token == '/':
                result = left / right
            stack.append(result)

    return stack.pop()

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = get_postfix(infix, len(infix))
    result = get_result(postfix)

    print(f'#{tc} {result}')