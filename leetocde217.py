class Solution():
    def countsDuplicate(self, nums):
        duplicates = []
        value = {}

        for num in nums:
            if num in value:
                value[num]+=1
            else:
                value[num]=1

        for num,count in value.items():
            if count>1:
                duplicates.append(num)

        if duplicates:
            return True
        else:
            return False
    
    
nums = [2,14,18,22,22]
solution = Solution()
result = solution.countsDuplicate(nums)

print(result) 
