#coding:utf-8

# 不得使用库函数,实现数值的整数次方

def Power(base, exponent):

    answer = 1.0

    if isEqualToZero(base, 0.0) == True:
        return False
    if exponent > 0:
        for i in range(exponent):
            answer *= base
        return answer
    elif exponent == 0:
        return 0
    elif exponent < 0:
        for i in range(exponent):
            answer *= base
        return 1/answer

def isEqualToZero(num1, num2): # 不能直接用==判断两个小数是否相等,两个小数的差值很小才能认为它们相等
    if (num1 - num2 < 0.0000001) and (num2 - num1 < 0.0000001):
        return True
    else:
        return False


print Power(5, 4)
print Power(0, -1)
