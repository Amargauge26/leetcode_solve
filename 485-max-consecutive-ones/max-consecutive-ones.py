class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi =0
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return 1 if nums[0]==1 else 0
        i =0
        while i < n:
            count = 0
            while i < n and nums[i] != 0:  # Corrected condition
                if nums[i] == 1:
                    count += 1
                i += 1
            maxi = max(maxi, count)
            i += 1
        return maxi

