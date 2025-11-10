class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h ={}
        for char in nums:
            if char not in h:
                h[char]=1
            else:
                h[char]+=1
        if any(value > 1 for value in h.values()) :
            return True
        return False