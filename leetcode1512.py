class Solution:
    def numIdenticalPairs(self, nums):
        pairs = {}
        count = 0

        for num in nums:
            if num in pairs:
                count+=pairs[num]
                pairs[num]+=1
            else:
                pairs[num]=1
        return count
nums = [1,2,3,1,1,3]
solution = Solution()
count_pairs = solution.numIdenticalPairs(nums)
print(count_pairs)