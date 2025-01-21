class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            # Check if target is at mid
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[l] <= nums[mid]:  # Left half is sorted
                if nums[l] <= target < nums[mid]:  # Target is in the left half
                    h = mid - 1
                else:  # Target is in the right half
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[h]:  # Target is in the right half
                    l = mid + 1
                else:  # Target is in the left half
                    h = mid - 1
        
        return -1  # Target not found
