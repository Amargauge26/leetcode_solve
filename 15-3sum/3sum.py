class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        n= len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            
            j=i+1
            k = n-1

            while j <k:
                sum=nums[i]+nums[j]+nums[k]

                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    ans.append(temp)
                    
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                    while k>j and nums[k]==nums[k+1]:
                        k-=1 
        
        return ans
                    