from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        psum=0

        d=defaultdict(int)
        count=0
        d[0]=1

        for i in range(n):
            psum+=nums[i]

            remove = psum-k

            count+=d[remove]

            d[psum]+=1
        return count