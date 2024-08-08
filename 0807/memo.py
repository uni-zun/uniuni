def fibo1(n):
    #global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 10
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo1(n))