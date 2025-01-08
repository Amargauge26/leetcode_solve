class Solution:
    def check(self, nums: List[int]) -> bool:
        ss = sorted(nums)
        for k in range(len(nums)):
            if nums[k:]+nums[:k]==ss:
                return True
        
        return False