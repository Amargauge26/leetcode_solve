class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2

        s = set(nums)
        for num in s:
            if nums.count(num)>(n):
                return num