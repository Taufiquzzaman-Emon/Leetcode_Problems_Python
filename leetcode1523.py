class Solution:
    def countOdds(self,low,high):
        count_high = (high+1)//2
        count_low = low//2
        return count_high-count_low
solution = Solution()
CountsOdd = solution.countOdds(3,7)
print(CountsOdd)
