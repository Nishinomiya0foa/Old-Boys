"""proceeding: 进程
定义：具有一定独立功能的程序关于某个数据集合的一次运行活动，是操作系统执行的基本单元。

"""

"""进程调度"""
# 先来先服务(FCFS):不利于短作业；适合CPU繁忙型作业
# 短作业有限:对长作业不利；不能保证紧迫性作业优先执行
# 时间片轮转：
# 多级反馈：优先级+时间片轮转；执行过1个时间片之后的任务会被轮转到下一优先级的队列中。短作业会更快被执行完，长作业会更久
            # 可设置优先级

"""进程的并行与并发
并行：两者同时并行，CPU数量>进程数
并发：多个进程交替在CPU上执行。 宏观上看起来仿佛是并行的
"""


"""进程的三态状态：
就绪：等待处理机执行
运行：处理机正在执行
阻塞：等待I/O完成、申请缓冲区不能满足、等待信件(信号)等，导致阻塞
"""

"""同步和异步
同步：一个任务的完成需要依赖另外一个任务，可靠。 两个任务的状态保持一致
异步：不需要等待被依赖的任务完成，不可靠。 两个任务的状态可能不一致
"""

"""阻塞和非阻塞

"""
class Solution:
    def twoSum(self, nums, target) -> list:
        new_nums = []
        for num in nums:
            if num <= target:
                new_nums.append(num)
        for num in new_nums:
            temp_new_nums = new_nums
            temp_new_nums.remove(num)
            for i in temp_new_nums:
                if num+i == target:
                    return [nums.index(num), temp_new_nums.index(i)+1]

getNum = Solution()
print(getNum.twoSum([2,5,5,11], 10))