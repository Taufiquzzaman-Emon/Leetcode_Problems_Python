class Solution:
    def validAnagram(self,s,t):

        anagram_list = {}

        # to define edge case of the process

        if len(s) != len(t):
            return False

        for n in (s):
            anagram_list[n] = anagram_list.get(n, 0) + 1
        for n in (t):
            if n in anagram_list:
                anagram_list[n]-=1
                if anagram_list[n]<0:
                    break
            else:
                return False
            
# If anagram_list = {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}, the all() check will return True because all values are 0.
# if anagram_list = {'a': 1, 'n': 0, 'g': 0, 'r': 0, 'm': 0}, the check will return False, because the count for 'a' is 1, meaning the strings are not anagrams.
        return all(value == 0 for value in anagram_list.values())
s  = "aacc"
t = "caca"

solution = Solution()
valid_anagram = solution.validAnagram(s,t)
print(valid_anagram)
