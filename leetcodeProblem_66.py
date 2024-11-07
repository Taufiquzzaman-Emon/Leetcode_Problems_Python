class Solution(object):
    def plusOne(self,digits):
        Combined_digits = int(''.join(str(num) for num in digits))
        Combined_digits+=1
        new_digits = [int(num) for num in str(Combined_digits)]
        return new_digits
digits = [4,3,2,1]
solution = Solution()
result = solution.plusOne(digits)
print(result)
                
