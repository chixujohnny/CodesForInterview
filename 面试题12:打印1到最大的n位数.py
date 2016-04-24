#coding:utf-8

# 面试题12:打印1到最大的n位数

import types

def SumEmulator(num): # num = '35499'

    i = len(num) - 1
    flag = 0
    lastNum = ''

    while True:
        if i == -1:
            return '1' + lastNum
        elif num[i] == '9':
            lastNum = '0' + lastNum
            i -= 1
        else:
            lastNum = str(int(num[i]) + 1) + lastNum
            return num[:i] + lastNum

def Print1ToMaxOfNDigits(num): # num = '35499'

    if num == '':
        return False
    else:
        i = 0
        while i <= int(num) - 1:
            print SumEmulator(str(i))
            i += 1
    return 0

Print1ToMaxOfNDigits('35967896786797948')



