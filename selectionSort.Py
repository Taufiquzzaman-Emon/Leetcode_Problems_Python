class Solution:
    def SelectionSort(self,nums):
        for i in range(len(nums)-1):
            SI = i
            for j in range(i+1,len(nums)):
                if (nums[j]<nums[SI]):
                    SI = j
            nums[i],nums[SI] = nums[SI],nums[i]
        return nums

nums = [4,1,3,2,5]
solution = Solution()
SSOrt = solution.SelectionSort(nums)
print(SSOrt)

    
