class Solution():
    def missingNumber(self,nums):
        sorted_nums = sorted(nums)

        for i,num in enumerate(sorted_nums):
            if i!=num:
                return i
        return len(nums)

nums = [0,1]
solution = Solution()
result = solution.missingNumber(nums)
print (result)