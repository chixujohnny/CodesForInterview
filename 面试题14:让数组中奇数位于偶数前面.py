#coding:utf-8

# 面试题14:让数组中的奇数位于偶数前面

def ReorderOddEven(data): # data: [1,2,3,4,5]
    p1 = 0 # 前指针
    p2 = len(data) - 1 # 后指针

    if p1 == p2:
        return False
    else:
        while True:
            if data[p1] % 2 == 1: # 如果p1位置的数是奇数
                p1 += 1
            else:
                if data[p2] % 2 == 0: # 如果p2位置的是偶数的话
                    p2 -= 1
                else:
                    if p1 > p2:
                        break
                    else: # 否则交换p1,p2的数字
                        flag = data[p1]
                        data[p1] = data[p2]
                        data[p2] = flag

        return data

data = [1,2,3,4,5]
print ReorderOddEven(data)
