# coding:utf-8

# 旋转数组的最小数字

def Min(dataList):

    flag1 = 0
    flag2 = len(dataList) - 1

    if dataList == []:
        return False

    elif dataList[flag1] < dataList[flag2]: # 特殊情况,此时数列严格递增
        return dataList[flag1]

    else:
        while flag1 +1 != flag2: # 当左指针刚好在相邻的左侧时结束循环
            if dataList[(flag1+flag2)/2] > dataList[flag1]: # 两指针中间数大于左数,min数在右侧
                flag1 = (flag1 + flag2) / 2 # 将左指针指向中间数
            else:
                flag2 = (flag1 + flag2) / 2 # 将右指针指向中间数
        return flag2

dataList = [3,4,5,6,1,2]
print Min(dataList)
