class Solution:
    def canMakeArithmeticProgression(self,arr):
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if arr[i + 1] - arr[i] != diff:
                return False
        return True
    
          
        
arr = [5,2,1]
solution = Solution()
ArithmeticProgression = solution.canMakeArithmeticProgression(arr)
print(ArithmeticProgression)