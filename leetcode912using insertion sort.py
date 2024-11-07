# class Solution(object):
#     def sortArray(self,nums):
#         for i in range(1, len(nums)):
#             j = i-1
#             while j>=0 and nums[j+1]<nums[j]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#                 j-=1
#         return nums 



# nums = [5,2,3,1]
# solution = Solution()
# sorted_nums = solution.sortArray(nums)
# print(sorted_nums)


class Solution():
    def sortArray(self,nums):
        for i in range(1,len(nums)):
            j = i-1
            while j>=0 and nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                j-=1
        return nums
nums = [2,1,2,3,4]
solution = Solution()
result = solution.sortArray(nums)
print(result)            