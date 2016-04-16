#coding:utf-8

# 连续子数组的最大和

def FindGreatestSumOfSubArray(dataList):

    if dataList == []:
        return False

    else:
        flag = sum = 0
        sumMax = -9999
        while flag < len(dataList):
            if sumMax == -9999: # 第一次遍历
                sum = sumMax = dataList[flag]
            else:
                if sum < 0: # 抛弃前面的sum
                    sum = dataList[flag]
                else:
                    sum += dataList[flag]
                    if sum > sumMax:
                        sumMax = sum
            flag += 1
        return sumMax

dataList = [1, -2, 3, 10, -4, 7, 2, -5]
print FindGreatestSumOfSubArray(dataList)

