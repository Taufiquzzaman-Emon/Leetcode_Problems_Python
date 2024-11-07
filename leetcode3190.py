class Solution:
    def minimumOperations(self,nums):
        operation = 0
        for i in range(len(nums)):
            if nums[i]%3==1:
                operation+=1
            elif nums[i]%3==2:
                operation+=1
        return operation
nums = [3,6,9]
solution = Solution()
Count_operations = solution.minimumOperations(nums)
print(Count_operations)


