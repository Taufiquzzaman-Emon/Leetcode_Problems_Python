class Solution(object):
    def sortArray(self,nums):
        self.nums = nums
        self.mergeSort(0,len(nums)-1)
        return self.nums
    def mergeSort(self,left,right):
        if left>=right:
            return
        mid = (left+right)//2
        self.mergeSort(left,mid)
        self.mergeSort(mid+1,right)
        self.merge(left,mid,right)
    
    def merge(self,left,mid,right):
        tempL = self.nums[left:mid+1]
        tempR = self.nums[mid+1:right+1]

        i = 0
        j = 0
        keypointer = left

        while i<len(tempL) and j<len(tempR):
            if tempL[i]<=tempR[j]:
                self.nums[keypointer] = tempL[i]
                i+=1
            else:
                self.nums[keypointer]=tempR[j]
                j+=1
            keypointer +=1

        while i < len(tempL):
            self.nums[keypointer] = tempL[i]
            i = i + 1
            keypointer = keypointer + 1
        while j < len(tempR):
            self.nums[keypointer] = tempR[j]
            j = j + 1
            keypointer = keypointer + 1

nums = [10,50,1,20,200,100,106,1009,20,21,40,150,4,0,3,202,11,11,191,2012,19,1992,10910,1982,223,202,1030,4435]
solution = Solution()
sort_Array = solution.sortArray(nums)
print(sort_Array)

          

    