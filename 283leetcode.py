class Solution:
    def moveZeroes(self,nums):

        i = 0
        j= 0
        while i<len(nums):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
            i+=1
        return nums

       

        
nums= [0,1,0,3,12]
solution = Solution()
zeroes = solution.moveZeroes(nums)
print(zeroes)

