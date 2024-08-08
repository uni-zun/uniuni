import sys
sys.stdin = open("input.txt", "r")

icp = {"+":1, "-":1, "*":2, "/":2, "(":3 }
isp = {"+":1, "-":1, "*":2, "/":2, "(":0 }

T = int(input())

for tc in range(1,T+1):
    str = input().split()

    stack = []
    for token in str:
        if token not in "+-*/.":
            stack.append(int(token))
        else:
            if len(stack) < 2:
                break
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
            if token == '//':
                result = left // right
            if token == '.':
                break

            stack.append(result)
    print(stack.pop())