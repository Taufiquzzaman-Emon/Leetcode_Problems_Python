class Solution:
    def majorityElement(self,nums):
        majority = {}
        
        for n in nums:
            if n in majority:
                majority[n]+=1
            else:
                majority[n]=1
            if majority[n] > len(nums) // 2:
                return n
nums = [3,2,3]
solution = Solution()
majority_element = solution.majorityElement(nums)
print(majority_element)
        
