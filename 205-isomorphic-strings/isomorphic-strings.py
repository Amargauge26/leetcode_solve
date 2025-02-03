class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s))!=len(set(t)):
            return False
        
        hash={}

        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = t[i]
            
            else:
                if hash[s[i]]!=t[i]:
                    return False
                
                """else:
                    hash[s[i]]=t[i]"""
        
        return True
