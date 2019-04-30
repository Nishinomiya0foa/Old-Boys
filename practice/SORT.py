"""冒泡"""
import time

# 乞丐版 冒泡排序
def get_bubbled(num_list,time=0):
    time += 1
    for i in range(len(num_list)):
        try:
            if num_list[i] >= num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

        except:
            if time < len(num_list):
                get_bubbled(num_list, time)
            else:
                print(num_list)
                return


# 非递归
def bubbleSort(myList):
    # 首先获取list的总长度,为之后的循环比较作准备
    length = len(myList)

    # 一共进行几轮列表比较,一共是(length-1)轮
    for i in range(0, length - 1):

        # 每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,注意-i的意义(可以减少比较已经排好序的元素)
        for j in range(0, length - 1 - i):

            # 交换
            if myList[j] > myList[j + 1]:
                tmp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = tmp

        # 打印每一轮交换后的列表
    print(myList)
    print("=============================")

if __name__ == '__main__':
    num_list = [1,4,2,5,3,-3,3,12,52,1,23,54,321,5431,321,41,1,2,-3,1,4,2,5,3,-3,3,12,52,1,23,54,321,5431,321,41,1,2,-3,1,4,2,5,3,-3,3,12,52,1,23,54,321,5431,321,41,1,2,-3,1,4,2,5,3,-3,3,12,52,1,23,54,321,5431,321,41,1,2,-3,]
    a = time.time()
    get_bubbled(num_list)
    # bubbleSort(num_list)
    print(time.time() - a)


a = {1:12,23:32,-1:'3'}
print(",".join(sorted(map(str, a.keys()))))



