class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen=0
        nums.sort()
        j =1
        if len(nums)<2:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1] :

                j+=1
            elif nums[i]==nums[i+1]:
                pass
            else:
                j=1
            
            maxlen = max(maxlen,j)
        
        return maxlen