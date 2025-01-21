class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadance impolimentation

        maxi =float("-inf")
        summ =0

        for i in range(len(nums)):
            summ+=nums[i]

            if summ>maxi:
                maxi =summ

            if summ<0:
                summ=0
        
        return maxi