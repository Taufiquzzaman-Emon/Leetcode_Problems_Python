class Solution:
    def binSearch(self,nums,key):
        l = 0
        h = len(nums)-1

        while(l<=h):
            mid = (l+h)//2
            if key == nums[mid]:
                return mid
            if key<nums[mid]:
                h = mid-1
            else:
                l = mid+1
        return l
    
nums = [1]
key = 0
solution = Solution()
key_Search = solution.binSearch(nums,key)
print(key_Search)
