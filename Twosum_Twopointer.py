class Solution(object):
    def twoSum(self,nums,target):
        numSorted = [(num,i) for i,num in enumerate(nums)]
        numSorted.sort()
        left ,right = 0,len(numSorted)-1
        while left<right:
            sum = numSorted[left][0]+numSorted[right][0]
            if sum==target:
                return [numSorted[left][1],numSorted[right][1]]
            elif sum<target:
                left+=1
            else:
                right-=1
        return None

nums = [3,2,4]
target = 6

solution = Solution()
result = solution.twoSum(nums,target)
print(result)