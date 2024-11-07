# Find the closest number to zero
class Solution(object):
    def findClosestNumber(self,nums):
        if not nums:
            return None
        closest = nums[0]

        for num in nums:
            if abs(num)<abs(closest) or (abs(num)==abs(closest) and num>closest):
                closest = num
        return closest



nums = [2,-1,1]
solution = Solution()
closest_num = solution.findClosestNumber(nums)
print(closest_num)
