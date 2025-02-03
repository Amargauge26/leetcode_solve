class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''

        cnt =0

        for char in s:
            if char=="(" :
                if cnt:
                    ans+=char
                
                cnt +=1
            
            else:
                cnt-=1
                if cnt:
                    ans+=char
        
        return ans