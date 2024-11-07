class Solution:
   def guessNumber(self,n):
      l,h = 1,n
      while l<=h:
         mid = (l+h)//2
         if mid == pick:
            return mid
         elif mid<pick:
            l =mid +1
         else:
            h = mid -1
pick = 10
solution = Solution()
guess = solution.guessNumber(10)
print(guess)