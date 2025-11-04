class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i , num in enumerate(nums):
            c = target -num
            if c in d:
                return [d[c],i]
            d[num]=i
        return []
        