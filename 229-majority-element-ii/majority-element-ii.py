class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash={}

        for i in nums:
            if i not in hash:
                hash[i]=1
            
            else:
                hash[i] += 1
        

        n = len(nums)

        ans=[]

        for val,count in hash.items():
            if count>(n/3):
                ans.append(val)
                print(count)
        return ans