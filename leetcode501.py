class Solution(object):
    def __init__(self):
        # initializing a dict() to store previously computed Fibonacci values to avoid redundant calculations
        self.memo = {}
    def fib(self,n):
    # checks whether the Fibonacci number for n has already been calculated and stored in the memo dictionary.
        if n in self.memo:
            return self.memo[n]
        if n<=1:
            return n
        
        self.memo[n] = self.fib(n-1)+self.fib(n-2)
        return self.memo[n]

n=1
solution = Solution()
Fibonacci = solution.fib(n)
print(Fibonacci)