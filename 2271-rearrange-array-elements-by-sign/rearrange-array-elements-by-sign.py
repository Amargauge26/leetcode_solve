class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        """f n<=2:
            nums.sort(reverse=True)
            return nums"""
        """if n>2:
            for i in range(n-2):
                if nums[i]>0 and nums[i+2]<0 or nums[i]<0 and nums[i+2]>0:
                    if nums[i+1]>0 and nums[i+2]<0 or nums[i+1]<0 and nums[i+2]>0:
                        nums[i+1],nums[i+2]=nums[i+2],nums[i+1]

        """     
        """p_ind =0
        n_ind = 1



        while p_ind<n and n_ind<n:
                while p_ind<n and nums[p_ind]>0:
                    p_ind+=2
                while n_ind<n and nums[n_ind]<0:
                    n_ind+=2
                

                if p_ind <n and n_ind<n:
                    nums[p_ind],nums[n_ind]=nums[n_ind],nums[p_ind]

                
            return nums"""

        pos= [num for num in nums if num>0]
        neg =  [ num for num in nums if num <0]


        i =0

        while pos or neg:
            if i%2==0 and pos:
                nums[i]=pos.pop(0)
            
            elif i%2!=0 and neg:
                nums[i]=neg.pop(0)
            i+=1

        return nums