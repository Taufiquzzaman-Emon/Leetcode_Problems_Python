class Solution(object):
    def __init__(self):
        self.stairs = {}
    def climbStairs(self,n):
        if n in self.stairs:
            return self.stairs[n]
        if n ==1:
            return 1
        if n == 0:
            return 1
        
        self.stairs[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.stairs[n]
    
n = 3
solution = Solution()
step_stairs = solution.climbStairs(n)
print(step_stairs)

