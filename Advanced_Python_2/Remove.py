class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0

        k = 0  # Pointer for the next non-val element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to the front
                k += 1  # Increment the count of non-val elements

        return k  # Return the number of elements not equal to val


# Example usage
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

solution = Solution()
count = solution.removeElement(nums, val)

print(count)  # Number of elements not equal to val
print(nums[:count])  # Updated array showing only elements not equal to val
