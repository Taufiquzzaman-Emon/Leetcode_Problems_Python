class Solution:
    def search(self,nums,target):
        l = 0
        h = len(nums)-1

        while l<=h:
            mid = (l+h)//2

            if nums[mid] == target:
                return mid

            elif nums[mid]<target:
                l = mid+1
            else:
                h = mid-1
        return -1 
    
nums = [-1,0,3,5,9,12]
solution =Solution()
_search = solution.search(nums,9)
print(_search)
