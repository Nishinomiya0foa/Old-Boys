# class Solution:
#     def twoSum(self, nums, target) -> list:
#         # new_nums = []
#         # for num in nums:
#         #     if num <= target:
#         #         new_nums.append(num)
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i]+nums[j] == target and i != j:
#                     return [i,j]

class Solution:
    def twoSum(self,nums, target):
        if len(nums) < 2:
            pass
        tempDict = {nums[0] : 0}  # -1
        for i in range(1, len(nums)):  # 1
            checkNum = target-nums[i]  # -1
            if checkNum in tempDict.keys():
                return [i,tempDict[checkNum]]  # [1, 0]
            else:
                tempDict[nums[i]] = i


getNum = Solution()
print(getNum.twoSum([-1,-2,-3,4,5], -3))