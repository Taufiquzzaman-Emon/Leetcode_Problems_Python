class Solution:
    def isPerfectSquare(self, nums):
        l = 0
        h = nums

        while l<=h:
            mid  = (l+h)//2
            if mid*mid == nums:
                return True
            elif mid * mid<nums:
                l = mid+1
            else:
                h = mid-1
        return False
solution = Solution()
pSquare = solution.isPerfectSquare(64)
print(pSquare)