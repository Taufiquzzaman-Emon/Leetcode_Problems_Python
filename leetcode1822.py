class Solution:
    def arraySign(self,nums):
        totalProduct = 1
        for num in nums:
            totalProduct*=num
        if totalProduct<0:
            return -1
        elif totalProduct>0:
            return 1
        elif totalProduct == 0:
            return 0

        
nums = [-1,1,-1,1,-1]
solution = Solution()
result = solution.arraySign(nums)
print(result)