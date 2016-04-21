# coding:utf-8

# 递归计算斐波那契数列

def FibonacciRecursion(n):
    if n < 0:
        return False
    elif n == 0:
        return 0
    else:
        FibonacciN = Fibonacci(n-1) +Fibonacci(n-2)
        return FibonacciN

# 循环计算斐波那契数列(相比递归更加高效)

def Fibonacci(n):
    num1 = 0; num2 = 1
    if n < 0:
        return False
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        i = 2
        while i <= n:
            numi = num1 + num2
            num1 = num2
            num2 = numi
            i += 1
        return numi

n = int(raw_input('请输入第几个斐波那契数:'))
print FibonacciRecursion(n-1)
print Fibonacci(n-1)