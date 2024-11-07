class Solution:
    def sortColors(self, nums):
        n = len(nums)

        for i in range(n):
            swapped = False #flag for early stopping if the list is already sorted
            for j in range(0, n - i - 1): 
                if nums[j] > nums[j + 1]: 
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break

        return nums


nums = [1,2,3]
solution = Solution()
ColorSort = solution.sortColors(nums)
print(ColorSort)
