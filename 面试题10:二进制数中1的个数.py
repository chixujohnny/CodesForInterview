#coding:utf-8

# 二进制数中1的个数

def NumberOf1(n): # 输入一个十进制数,输出这个数二进制数中1的个数
    flag = 1; count = 0
    while flag <= 2**31-1: # 由于python能表示大数,因此设置一下传统int型的数值上限
        if n & flag:
            count += 1
        flag = flag << 1
    return count

n = int(raw_input('请输入十进制数,我会输出这个十进制数的二进制数中1的个数:'))
print NumberOf1(n)