class Solution:
    def nextGreatestLetter(self,letters,target):
        l = 0
        h= len(letters)-1
        while l<=h:
            mid = (l+h)//2
            if letters[mid]>target:
                h = mid-1
            else:
                l= mid+1
        return letters[l] if l<len(letters) else letters[0]
letters =["x","x","y","y"]
solution = Solution()
greatest_letter = solution.nextGreatestLetter(letters,"z")
print(greatest_letter)
