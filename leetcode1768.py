# Merge Strings Alternately

class Solution(object):
    def mergeAlternately(self,word1,word2):
        merged= []
        left = 0
        right = 0
        while left < len(word1) or right < len(word2):
            if left<len(word1):
                merged.append(word1[left])
                left+=1
            if right<len(word2):
                merged.append(word2[right])
                right+=1
        return ''.join(merged)
   
word1 = "ab"
word2 ="pqrs"
solution= Solution()
merged_word = solution.mergeAlternately(word1,word2)
print(merged_word)