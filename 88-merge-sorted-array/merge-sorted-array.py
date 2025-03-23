class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = [0] * (m + n)
    
        # Pointers for nums1 and nums2
        i = 0  # Pointer for nums1
        j = 0  # Pointer for nums2
        k = 0  # Pointer for temp array
        
        # Merge the two arrays into temp
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp[k] = nums1[i]
                i += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1
        
        # If there are remaining elements in nums1
        while i < m:
            temp[k] = nums1[i]
            i += 1
            k += 1
        
        # If there are remaining elements in nums2
        while j < n:
            temp[k] = nums2[j]
            j += 1
            k += 1
        
        # Copy the merged values back to nums1
        for i in range(m + n):
            nums1[i] = temp[i]