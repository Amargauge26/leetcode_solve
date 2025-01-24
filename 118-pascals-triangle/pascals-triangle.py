class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans =[[1]]
        for i in range(1,numRows):
            mid=[]
            temp = ans[-1]
            temp = [0]+temp+[0]
            
            for j in range(len(temp)-1):
                val = temp[j]+temp[j+1]
                mid.append(val)
            
            ans.append(mid)
    
        return ans