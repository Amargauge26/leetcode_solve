class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for char in nums:
            if char in hash:
                
                return True
            hash[char]=1
        
        return False