class Solution():
    def minElement(self,nums):
        num = ', '.join(str(num) for num in nums)
        for i, nums in enumerate(num):
            sum = num + num



nums = [12,22,31,41]
solution = Solution()
result = solution.minElement(nums)
print(result)

