from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = Counter(nums)


        for i in range(d[0]):
            nums[i]=0
        for j in range(d[0],d[0]+d[1]):
            nums[j]=1
        
        for k in range(d[0]+d[1],d[0]+d[1]+d[2]):
            nums[k]=2
        return nums