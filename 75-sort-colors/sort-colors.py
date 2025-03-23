from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """d = Counter(nums)


        for i in range(d[0]):
            nums[i]=0
        for j in range(d[0],d[0]+d[1]):
            nums[j]=1
        
        for k in range(d[0]+d[1],d[0]+d[1]+d[2]):
            nums[k]=2
        return nums"""

        #ducthnational flag aklgo

        """n = len(nums)
        low =0
        mid =0
        high = n-1

        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            
            elif nums[mid]==1:
                mid+=1
            
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        

        return nums"""
        nums.sort()
                                                                        

