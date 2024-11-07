class Solution():
    def isValid(self,s):
        opening_brace = ["(","{","["]
        closing_brace = [")","}","]"]
        stack = []

        for char in s:
            if char in opening_brace:
                stack.append(char)

            elif char in closing_brace:
                if not stack:
                    return False
                top = stack.pop()
                if opening_brace.index(top)!=closing_brace.index(char):
                        return False
        return len(stack) == 0

s = ["(}", "{}", "[]"] 
solution = Solution()
is_valid = [solution.isValid(pair) for pair in s]
print(is_valid)