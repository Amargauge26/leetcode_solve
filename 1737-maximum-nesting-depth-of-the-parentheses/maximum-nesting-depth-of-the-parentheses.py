class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=0
        currdep=0

        for char in s:
            if char =="(":
                currdep+=1
                maxi = max(maxi,currdep)
            
            elif char ==")":
                currdep-=1
            
        
        return maxi
        