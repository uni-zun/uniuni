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

infix = '(6+5*(2-8)/2)'
postfix = get_postfix(infix, len(infix))
print(postfix)

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

result = get_result(postfix)

print(result)