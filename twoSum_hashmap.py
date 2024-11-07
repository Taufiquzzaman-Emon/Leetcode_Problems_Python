class Solution():
    def twoSum(self,nums,target):
        value = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in value:
                return[value[diff],i]
            value[n]= i




nums = [2,7,15,11]
target = 9

solution = Solution()
result = solution.twoSum(nums,target)
print(result)