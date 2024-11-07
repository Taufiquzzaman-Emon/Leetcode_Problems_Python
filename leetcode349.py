class Solution:
    def intersection(self,nums1,nums2):
        unique_element = {}

        for n in nums1:
            if n not in unique_element:
                unique_element[n]=1
        result = set()

        for n1 in nums2:
            if n1 in unique_element:
                result.add(n1)
        return list(result)

nums1 = [1,2,2,1]
nums2 = [2,3]
solution = Solution()
Intersection = solution.intersection(nums1,nums2)
print(Intersection)

