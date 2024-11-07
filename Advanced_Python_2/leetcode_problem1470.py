class Solution():
    def shuffle(self,nums,n):

        shuffled = []
        for i in range(n):
            shuffled.append (nums[i])
            shuffled.append(nums[n+i])
        return shuffled

nums = [2,5,1,3,4,7]
n = 3
solution = Solution()
shuffledArray = solution.shuffle(nums,n)
print(shuffledArray)




