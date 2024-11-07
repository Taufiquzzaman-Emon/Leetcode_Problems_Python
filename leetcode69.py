class Solution:
    def mySqrt(self,x):
        l = 1
        h = x
        
        while l<=h:
            mid = (l+h)//2
            if mid*mid == x:
                return mid
            elif mid*mid<x:
                l = mid+1
            else:
                h = mid-1
        return h

solution = Solution()
sQRT = solution.mySqrt(16)
print(sQRT)