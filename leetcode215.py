import random

class Solution:
    def findKthLargest(self, nums, k):
        # We need the Kth largest element, so we look for the (n - k)th index
        target_index = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, target_index)

    def quickSelect(self, nums, low, high, target_index):
        if low <= high:
            pivot_index = self.partition(nums, low, high)

            # If the pivot is at the target index, we will return the value
            if pivot_index == target_index:
                return nums[pivot_index]
            # If the pivot is greater than the target index, recursing on the left side
            elif pivot_index > target_index:
                return self.quickSelect(nums, low, pivot_index - 1, target_index)
            # Otherwise, we will recurse on the right side
            else:
                return self.quickSelect(nums, pivot_index + 1, high, target_index)

    def partition(self, nums, low, high):
        
        rand_pivot = random.randint(low, high)
        nums[low], nums[rand_pivot] = nums[rand_pivot], nums[low]  # This moves the pivot to start

        pivot = nums[low]
        i = low + 1
        j = high

        while True:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        nums[low], nums[j] = nums[j], nums[low]
        return j

# Example usage
nums = [3, 2, 1, 5, 6, 4]
solution = Solution()
Kth_element = solution.findKthLargest(nums, 2)
print(Kth_element)
